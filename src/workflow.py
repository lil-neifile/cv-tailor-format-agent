from langgraph.graph import StateGraph, START, END

from .graph.nodes import tailor_cv, build_html, build_PDF, analyze_job_description, compare_cv_with_job_description, fry_applicant, inspire_applicant
from .graph.state import CVAgentState

graph = StateGraph(CVAgentState)

graph.add_node("tailor_cv", tailor_cv)
graph.add_node("build_html", build_html)
graph.add_node("build_PDF", build_PDF)
graph.add_node("analyze_job_description", analyze_job_description)
graph.add_node("compare_cv_with_job_description", compare_cv_with_job_description)
graph.add_node("fry_applicant", fry_applicant)
graph.add_node("inspire_applicant", inspire_applicant)

graph.add_edge(START, "analyze_job_description")
graph.add_edge("analyze_job_description", "compare_cv_with_job_description")
graph.add_edge("compare_cv_with_job_description", "tailor_cv")
graph.add_edge("tailor_cv", "build_html")
graph.add_edge("build_html", "build_PDF")
graph.add_edge("build_PDF", "fry_applicant")
graph.add_edge("fry_applicant", "inspire_applicant")
graph.add_edge("inspire_applicant", END)

compiled_graph = graph.compile()