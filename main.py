import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import streamlit as st
from streamlit_extras.let_it_rain import rain

from src.services.cv_parser import CVParser
from src.workflow_agent import compiled_agent

logger.info("Starting Streamlit app")
st.title("CV Agent")

cv_file = st.file_uploader("Upload CV", type=["pdf"])

if cv_file:
    logger.info("Uploading CV")
    cv_bytes = cv_file.getvalue()
    cv_string = CVParser().parse(cv_bytes)
    
    logger.info("CV uploaded successfully")
job_description = st.text_area("Job Description")

if st.button("Tailor CV"):
    logger.info("Tailoring CV")
    if not cv_string or not job_description:
        st.error("Please upload a CV and enter a job description", icon="🚨")
        st.stop()
    logger.info("CV and job description are valid")
    try:
        tailored_cv = compiled_agent.invoke({
        "cv": cv_string,
            "job_description": job_description,
        })
        pdf_bytes = tailored_cv["pdf_bytes"]
        logger.info("CV tailored successfully")
    except Exception as e:
        logger.error(f"Error tailoring CV: {e}", exc_info=True)
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
        logger.error(f"Error building PDF: {e}", exc_info=True)
        st.error(f"Error building PDF: {e}", icon="🚨")

    try:
        st.html(tailored_cv["html_content"])
    except Exception as e:
        logger.error(f"Error building HTML: {e}", exc_info=True)
        st.error(f"Error building HTML: {e}", icon="🚨")

    try:
        fry_applicant_content = tailored_cv["mock"]
        st.markdown("## Fry Applicant Content")
        st.markdown(fry_applicant_content)
    except Exception as e:
        logger.error(f"Error getting fry applicant: {e}", exc_info=True)
        st.error(f"Error getting fry applicant: {e}", icon="🚨")
        raise

    try:
        inspire_applicant_content = tailored_cv["inspiration"]
        st.markdown("## Inspire Applicant Content")
        st.markdown(inspire_applicant_content)
    except Exception as e:
        logger.error(f"Error getting inspire applicant: {e}", exc_info=True)
        st.error(f"Error getting inspire applicant: {e}", icon="🚨")
        raise
    
    rain(
    emoji="🌈",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)