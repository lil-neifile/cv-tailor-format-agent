from langgraph.graph import StateGraph, START, END

from .graph.nodes import tailor_cv, build_html, build_PDF, analyze_job_description, compare_cv_with_job_description, fry_applicant, inspire_applicant
from .graph.state import CVAgentState

graph_divided = StateGraph(CVAgentState)

graph_divided.add_node("tailor_cv", tailor_cv)
graph_divided.add_node("build_html", build_html)
graph_divided.add_node("build_PDF", build_PDF)
graph_divided.add_node("analyze_job_description", analyze_job_description)
graph_divided.add_node("compare_cv_with_job_description", compare_cv_with_job_description)
graph_divided.add_node("fry_applicant", fry_applicant)
graph_divided.add_node("inspire_applicant", inspire_applicant)

graph_divided.add_edge(START, "analyze_job_description")
graph_divided.add_edge("analyze_job_description", "compare_cv_with_job_description")
graph_divided.add_edge("compare_cv_with_job_description", "tailor_cv")
graph_divided.add_edge("tailor_cv", "build_html")
graph_divided.add_edge("build_html", "build_PDF")
graph_divided.add_edge("build_PDF", "fry_applicant")
graph_divided.add_edge("fry_applicant", "inspire_applicant")
graph_divided.add_edge("inspire_applicant", END)

compiled_graph_divided = graph_divided.compile()