import streamlit as st
from src.workflow_agent import compiled_agent
from tests.test_tailor_cv_node import BASE_CV
from streamlit_extras.let_it_rain import rain


st.title("CV Agent")

job_description = st.text_area("Job Description")

if st.button("Tailor CV"):

    try:
        tailored_cv = compiled_agent.invoke({
        "cv": BASE_CV,
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