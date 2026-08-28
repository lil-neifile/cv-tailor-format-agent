# using streamlit a window that will take a job description and show a tailored cv
import streamlit as st
from tests.test_tailor_cv_node import BASE_CV
from src.workflow import compiled_graph
from streamlit_extras.let_it_rain import *


st.title("Tailored CV")

job_description = st.text_area("Job Description")

if st.button("Tailor CV"):

    
    tailored_cv = compiled_graph.invoke({
        "base_cv_text": BASE_CV,
        "job_description": job_description,
    })
    pdf_bytes = tailored_cv["pdf_bytes"]
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


    fry_applicant_content = tailored_cv["fry_applicant_content"]
    inspire_applicant_content = tailored_cv["inspire_applicant_content"]
    st.markdown("## Fry Applicant Content")
    st.markdown(fry_applicant_content)
    st.markdown("## Inspire Applicant Content")
    st.markdown(inspire_applicant_content)

    rain(
    emoji="🌈",
    font_size=54,
    falling_speed=5,
    animation_length="infinite",
)
