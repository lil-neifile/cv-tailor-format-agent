from src.graph.nodes import build_html

TAILORED_CONTENT = {
    "header": {
        "name": "Lili Herrera",
        "title": "AI Engineer",
        "email": "lili.herrera@gmail.com",
        "phone": "",
        "location": "San Francisco, CA",
        "linkedin": "",
        "website": "",
    },
    "summary": (
        "AI Engineer with experience building production ML systems, LLM applications, "
        "and cloud-native deployments."
    ),
    "experience": [
        {
            "title": "Senior Developer",
            "company": "Tech Corp",
            "location": "San Francisco, CA",
            "dates": "2020 - Present",
            "bullets": [
                "Built ML pipelines with TensorFlow and scikit-learn",
                "Deployed models using Docker and Kubernetes on AWS",
            ],
        }
    ],
    "skills": ["Python", "LangChain", "LangGraph", "Docker", "Kubernetes"],
    "education": [
        {
            "degree": "B.S. Computer Science",
            "school": "State University",
            "dates": "2014 - 2018",
            "details": "",
        }
    ],
}


def test_format_tailored_content_node_outputs_results():
    result = build_html({"tailored_content": TAILORED_CONTENT})
    print(result["html_content"])
