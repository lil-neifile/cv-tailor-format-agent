import json

from src.graph.nodes import analyze_job_description
from tests.test_tailor_cv_node import JOB_DESCRIPTION


def test_analyze_job_description_node_outputs_results():
    result = analyze_job_description({"job_description": JOB_DESCRIPTION})
    print(json.dumps(result, indent=2, ensure_ascii=False))
