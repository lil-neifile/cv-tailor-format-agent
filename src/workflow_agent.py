from langgraph.graph import END, START, StateGraph

from .agent.nodes_agent import llm_call_node, should_continue, tool_call_node
from .agent.state_agent import CVAgentDynamicState
from langgraph.types import RetryPolicy, TimeoutPolicy

agent_builder = StateGraph(CVAgentDynamicState)

agent_builder.add_node("llm_call_node", llm_call_node, retry_policy=RetryPolicy(max_attempts=2), timeout_policy=TimeoutPolicy(idle_timeout=30))
agent_builder.add_node("tool_call_node", tool_call_node, retry_policy=RetryPolicy(max_attempts=2), timeout_policy=TimeoutPolicy(idle_timeout=120))

agent_builder.add_edge(START, "llm_call_node")
agent_builder.add_conditional_edges(
    "llm_call_node",
    should_continue,
    ["tool_call_node", END],
)
agent_builder.add_edge("tool_call_node", "llm_call_node")

compiled_agent = agent_builder.compile()
