from langchain.messages import ToolMessage
from langchain.tools import ToolRuntime, tool
from langgraph.types import Command

from src.agent.prompts_agent import TAILOR_CV_DYNAMIC_SYSTEM
from src.agent.state_agent import CVAgentDynamicState
from src.graph.prompts import FRY_APPLICANT_SYSTEM, INSPIRE_APPLICANT_SYSTEM
from src.schemas import TailoredCVDynamic
from src.services.llm import get_llm, invoke_chat, invoke_structured
from src.services.pdf_builder import HTMLBuilder

CVToolRuntime = ToolRuntime[None, CVAgentDynamicState]


def _tool_message(text: str, runtime: CVToolRuntime) -> ToolMessage:
    return ToolMessage(content=text, tool_call_id=runtime.tool_call_id)


@tool
def tailor_cv(runtime: CVToolRuntime) -> Command:
    """Rewrite the applicant's CV so that it matches the job description.

    Reads the CV and the job description from the agent state, so it takes no arguments.
    Run this before build_html, inspire_applicant or fry_applicant.
    """
    result = invoke_structured(
        TailoredCVDynamic,
        system=TAILOR_CV_DYNAMIC_SYSTEM,
        user=(
            f"JOB DESCRIPTION:\n{runtime.state['job_description']}\n\n"
            f"CV:\n{runtime.state['cv']}"
        ),
        max_tokens=4000,
    )
    return Command(
        update={
            "tailored_content": result.tailored_content.model_dump(),
            "keywords_matched": result.keywords_matched,
            "keywords_not_matched": result.keywords_not_matched,
            "messages": [
                _tool_message(
                    "Tailored the CV. "
                    f"Matched keywords: {', '.join(result.keywords_matched) or 'none'}. "
                    f"Missing keywords: {', '.join(result.keywords_not_matched) or 'none'}.",
                    runtime,
                )
            ],
        }
    )


@tool
def build_html(runtime: CVToolRuntime) -> Command | str:
    """Render the tailored CV into a styled HTML document.

    Requires tailor_cv to have run first. Takes no arguments.
    """
    tailored_content = runtime.state.get("tailored_content")
    if not tailored_content:
        return "There is no tailored CV yet. Call tailor_cv first."

    html_content = HTMLBuilder().build_html(**tailored_content)
    return Command(
        update={
            "html_content": html_content,
            "messages": [
                _tool_message(
                    f"Built the HTML CV ({len(html_content)} characters). It is saved for the applicant.",
                    runtime,
                )
            ],
        }
    )


@tool
def build_pdf(runtime: CVToolRuntime) -> Command | str:
    """Render the HTML CV into a downloadable PDF.

    Requires build_html to have run first. Takes no arguments.
    """
    html_content = runtime.state.get("html_content")
    if not html_content:
        return "There is no HTML CV yet. Call build_html first."

    pdf_bytes = HTMLBuilder().build_pdf(html_content)
    return Command(
        update={
            "pdf_bytes": pdf_bytes,
            "messages": [
                _tool_message(
                    f"Built the PDF CV ({len(pdf_bytes)} bytes). It is saved for download.",
                    runtime,
                )
            ],
        }
    )


@tool
def fry_applicant(runtime: CVToolRuntime) -> Command | str:
    """Roast the applicant about the job-description keywords their CV is missing.

    Requires tailor_cv to have run first. Takes no arguments.
    """
    keywords_not_matched = runtime.state.get("keywords_not_matched")
    if not keywords_not_matched:
        return "The missing keywords are not known yet. Call tailor_cv first."

    content = invoke_chat(
        system=FRY_APPLICANT_SYSTEM,
        user="\n".join(keywords_not_matched),
        max_tokens=500,
    ).text
    return Command(
        update={
            "mock": content,
            "messages": [_tool_message(content, runtime)],
        }
    )


@tool
def inspire_applicant(runtime: CVToolRuntime) -> Command | str:
    """Hype the applicant up about the job-description keywords their CV already matches.

    Requires tailor_cv to have run first. Takes no arguments.
    """
    keywords_matched = runtime.state.get("keywords_matched")
    if not keywords_matched:
        return "The matched keywords are not known yet. Call tailor_cv first."

    content = invoke_chat(
        system=INSPIRE_APPLICANT_SYSTEM,
        user="\n".join(keywords_matched),
        max_tokens=500,
    ).text
    return Command(
        update={
            "inspiration": content,
            "messages": [_tool_message(content, runtime)],
        }
    )


tools = [tailor_cv, build_html, build_pdf, fry_applicant, inspire_applicant]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = get_llm().bind_tools(tools)
