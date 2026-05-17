import streamlit as st
from resume_parser import extract_text
from job_recommender import recommend_jobs

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    st.subheader("Resume Text")
    st.write(text[:1000])

    jobs = recommend_jobs(text)

    st.subheader("Recommended Jobs")

    for job in jobs:
        st.write("✔", job)