import streamlit as st
from src.workflow_agent import compiled_agent
from tests.test_tailor_cv_node import BASE_CV
from streamlit_extras.let_it_rain import rain
from src.services.cv_parser import CVParser

st.title("CV Agent")

cv_file = st.file_uploader("Upload CV", type=["pdf"])

if cv_file:
    cv_bytes = cv_file.getvalue()
    cv_string = CVParser().parse(cv_bytes)
    

job_description = st.text_area("Job Description")

if st.button("Tailor CV"):
    if not cv_string or not job_description:
        st.error("Please upload a CV and enter a job description", icon="🚨")
        st.stop()
    
    try:
        tailored_cv = compiled_agent.invoke({
        "cv": cv_string,
            "job_description": job_description,
        })
        pdf_bytes = tailored_cv["pdf_bytes"]
    except Exception as e:
        st.error(f"Error tailoring CV: {e}", icon="🚨")
        raise
    
    try:
        st.download_button(
            label="📥 Download PDF Document",
            data=pdf_bytes,
            file_name="tailored_cv.pdf",
            mime="application/pdf",
        )
    except Exception as e:
        st.error(f"Error building PDF: {e}", icon="🚨")

    try:
        st.html(tailored_cv["html_content"])
    except Exception as e:
        st.error(f"Error building HTML: {e}")

    try:
        fry_applicant_content = tailored_cv["mock"]
        st.markdown("## Fry Applicant Content")
        st.markdown(fry_applicant_content)
    except Exception as e:
        st.error(f"Error getting fry applicant: {e}", icon="🚨")
        raise

    try:
        inspire_applicant_content = tailored_cv["inspiration"]
        st.markdown("## Inspire Applicant Content")
        st.markdown(inspire_applicant_content)
    except Exception as e:
        st.error(f"Error getting inspire applicant: {e}", icon="🚨")
        raise
    
    rain(
    emoji="🌈",
    font_size=54,
    falling_speed=5,
    animation_length="short",
)