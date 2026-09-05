import sys

REPO = "/Users/liliiashrainer/Desktop/Coloss Folder/Personal/cv-tailor-format-agent"
sys.path.insert(0, REPO)

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.outputs import ChatGeneration, ChatResult

import src.services.llm as llm_mod
from src.schemas import TailoredContent, TailoredCVDynamic

SCRIPT = []
CURSOR = {"i": 0}


class ScriptedModel(BaseChatModel):
    def _generate(self, messages, stop=None, run_manager=None, **kwargs):
        msg = SCRIPT[CURSOR["i"]]
        CURSOR["i"] += 1
        return ChatResult(generations=[ChatGeneration(message=msg)])

    @property
    def _llm_type(self):
        return "scripted"

    def bind_tools(self, tools, **kwargs):
        return self


def fake_structured(schema, system, user, max_tokens):
    assert "JOB DESCRIPTION:" in user and "CV:" in user, "tool must read state"
    return TailoredCVDynamic(
        tailored_content=TailoredContent(
            summary="Tailored summary.",
            skills=["Python", "LangGraph"],
        ),
        keywords_matched=["Python", "LangGraph"],
        keywords_not_matched=["Kubernetes"],
    )


def fake_chat(system, user, max_tokens=None):
    return AIMessage(content=f"scripted reply for: {user}")


llm_mod.get_llm = lambda max_tokens=None: ScriptedModel()
llm_mod.invoke_structured = fake_structured
llm_mod.invoke_chat = fake_chat

from src.services.pdf_builder import HTMLBuilder

HTMLBuilder.build_pdf = lambda self, html: b"%PDF-1.4 fake bytes"

from src.workflow_agent import compiled_agent


def call(name, id_):
    return AIMessage(content="", tool_calls=[{"name": name, "args": {}, "id": id_}])


def run(script, label):
    SCRIPT.clear()
    SCRIPT.extend(script)
    CURSOR["i"] = 0
    result = compiled_agent.invoke(
        {
            "messages": [HumanMessage("Here is the job description: AI Engineer, Python.")],
            "cv": "Liliia Shrainer, AI Engineer, Python, LangGraph.",
            "job_description": "AI Engineer, Python, LangGraph, Kubernetes.",
        }
    )
    print(f"\n===== {label} =====")
    for m in result["messages"]:
        m.pretty_print()
    print("--- state artifacts ---")
    for key in (
        "tailored_content",
        "keywords_matched",
        "keywords_not_matched",
        "html_content",
        "pdf_bytes",
        "mock",
        "inspiration",
    ):
        value = result.get(key)
        shown = f"{type(value).__name__} len={len(value)}" if isinstance(value, (str, bytes)) else value
        print(f"{key}: {shown}")
    return result


happy = run(
    [
        call("tailor_cv", "1"),
        call("build_html", "2"),
        call("build_pdf", "3"),
        call("inspire_applicant", "4"),
        call("fry_applicant", "5"),
        AIMessage(content="All done, your CV is ready."),
    ],
    "happy path",
)

assert happy["tailored_content"]["summary"] == "Tailored summary."
assert happy["html_content"].startswith("<!DOCTYPE html>")
assert "Tailored summary." in happy["html_content"]
assert happy["pdf_bytes"] == b"%PDF-1.4 fake bytes"
assert happy["mock"] and happy["inspiration"]
assert all(isinstance(m.content, str) for m in happy["messages"])

out_of_order = run(
    [
        call("build_html", "1"),
        call("tailor_cv", "2"),
        call("build_html", "3"),
        AIMessage(content="Recovered."),
    ],
    "out of order (guard path)",
)

assert "Call tailor_cv first." in out_of_order["messages"][2].content
assert out_of_order["html_content"].startswith("<!DOCTYPE html>")

print("\nALL ASSERTIONS PASSED")
