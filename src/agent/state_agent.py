from typing import NotRequired

from langchain.agents import AgentState


class CVAgentDynamicState(AgentState):
    """Agent scratchpad (`messages`, inherited) plus the artifacts the tools produce.

    `cv` and `job_description` are seeded at invoke time so the model never has to
    retype them into tool arguments; tools read them through `ToolRuntime.state`.
    """

    cv: str
    job_description: str

    tailored_content: NotRequired[dict]
    keywords_matched: NotRequired[list[str]]
    keywords_not_matched: NotRequired[list[str]]
    html_content: NotRequired[str]
    pdf_bytes: NotRequired[bytes]
    mock: NotRequired[str]
    inspiration: NotRequired[str]
