from typing import Literal

from langchain.messages import SystemMessage
from langgraph.graph import END
from langgraph.prebuilt import ToolNode

from src.agent.prompts_agent import CV_AGENT_SYSTEM
from src.agent.state_agent import CVAgentDynamicState
from src.agent.tools import llm_with_tools, tools


def llm_call_node(state: CVAgentDynamicState) -> dict:
    """Let the model pick the next tool call, or finish with an answer."""
    return {
        "messages": [
            llm_with_tools.invoke(
                [SystemMessage(content=CV_AGENT_SYSTEM), *state["messages"]]
            )
        ]
    }


# ToolNode injects ToolRuntime and merges the Command state updates the tools return.
# A hand-written loop would have to propagate those updates itself.
tool_call_node = ToolNode(tools)


def should_continue(state: CVAgentDynamicState) -> Literal["tool_call_node", "__end__"]:
    """Keep looping while the model requests tools, otherwise reply to the user."""
    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tool_call_node"

    return END
