from ..schemas import TailoredContent, JobDescriptionAnalyzer, CompareCVWithJobDescription
from .state import CVAgentState
from ..services.llm import invoke_structured, invoke_chat
from .prompts import TAILOR_CV_SYSTEM, JOB_DESCRIPTION_ANALYZER_SYSTEM, COMPARE_CV_WITH_JOB_DESCRIPTION_SYSTEM, FRY_APPLICANT_SYSTEM, INSPIRE_APPLICANT_SYSTEM
from ..services.pdf_builder import HTMLBuilder
import json


def analyze_job_description(state: CVAgentState) -> dict:
    content = invoke_structured(
        JobDescriptionAnalyzer,
        system=JOB_DESCRIPTION_ANALYZER_SYSTEM,
        user=state['job_description'],
        max_tokens=1000
    )
    return {
        "job_description_analysis": content.model_dump()
    }


def compare_cv_with_job_description(state: CVAgentState) -> dict:
    content = invoke_structured(
        CompareCVWithJobDescription,
        system=COMPARE_CV_WITH_JOB_DESCRIPTION_SYSTEM,
        user=(
            "JOB DESCRIPTION ANALYSIS:\n"
            f"{json.dumps(state['job_description_analysis'])}\n\n"
            "CV:\n"
            f"{state['base_cv_text']}"
        ),
        max_tokens=1000
    )
    return {
        "skills_match": content.model_dump()["skills_match"],
        "skills_present_importance_lower_than_expected": content.model_dump()["skills_present_importance_lower_than_expected"],
        "skills_present_different_wording": content.model_dump()["skills_present_different_wording"],
        "skills_missing": content.model_dump()["skills_missing"],
    }

def tailor_cv(state: CVAgentState) -> dict:

    content = invoke_structured(
        TailoredContent,
        system=TAILOR_CV_SYSTEM,
        user=(
            "Skills to match:\n"
            f"{state['skills_match']}\n\n"
            "Skills present importance lower than expected:\n"
            f"{state['skills_present_importance_lower_than_expected']}\n\n"
            "Skills present different wording:\n"
            f"{state['skills_present_different_wording']}\n\n"
            "Skills missing:\n"
            f"{state['skills_missing']}\n\n"
            "SOURCE CV:\n"
            f"{state['base_cv_text']}"
        ),
        max_tokens=None

    )
    return {
        "tailored_content": content.model_dump()
    }

def build_html(state: CVAgentState) -> dict:
    html_content = HTMLBuilder().build_html(**state['tailored_content'])
    return {
        "html_content": html_content
    }

def build_PDF(state: CVAgentState) -> dict:
    pdf_bytes = HTMLBuilder().build_pdf(state['html_content'])
    return {
        "pdf_bytes": pdf_bytes
    }

def fry_applicant(state: CVAgentState) -> dict:
    content = invoke_chat(
        system=FRY_APPLICANT_SYSTEM,
        user=state['skills_missing'],
        max_tokens=500
    )
    return {
        "fry_applicant_content": content
    }

def inspire_applicant(state: CVAgentState) -> dict:
    content = invoke_chat(
        system=INSPIRE_APPLICANT_SYSTEM,
        user=state['skills_match'],
        max_tokens=500
    )
    return {
        "inspire_applicant_content": content
    }