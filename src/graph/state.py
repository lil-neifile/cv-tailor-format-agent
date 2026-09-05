from typing import TypedDict


class CVAgentState(TypedDict, total=False):
    base_cv_text: str
    job_description: str
    job_description_analysis: dict
    cv_job_comparison: dict
    skills_match: list[str]
    skills_present_importance_lower_than_expected: list[str]
    skills_present_different_wording: list[str]
    skills_missing: list[str]
    tailored_content: dict
    html_content: str
    pdf_bytes: bytes
    fry_applicant_content: str
    inspire_applicant_content: str
    errors: list[str]

