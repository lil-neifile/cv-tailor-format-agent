from typing import NotRequired

from langchain.agents import AgentState

from src.schemas import TailoredContent


class CVAgentDynamicState(AgentState):
    """Agent scratchpad (`messages`, inherited) plus the artifacts the tools produce.

    `cv` and `job_description` are seeded at invoke time so the model never has to
    retype them into tool arguments; tools read them through `ToolRuntime.state`.
    """

    cv: str
    job_description: str

    tailored_content: TailoredContent
    keywords_matched: list[str]
    keywords_not_matched: list[str]
    html_content: str
    pdf_bytes: bytes
    mock: str
    inspiration: str
