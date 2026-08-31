
import streamlit as st
import pandas as pd

from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from resume_scorer import calculate_resume_score, get_missing_skills
from job_recommender import recommend_jobs


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")
st.write("Upload your resume to analyze your skills and find suitable jobs.")


uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)


if uploaded_file:

    # --------------------------------
    # 1. Extract resume text
    # --------------------------------
    text = extract_text_from_pdf(uploaded_file)


    # --------------------------------
    # 2. Extract skills
    # --------------------------------
    skills = extract_skills(text)

    st.subheader("🧠 Detected Skills")

    if skills:
        st.write(", ".join(skills))
    else:
        st.warning("No skills detected.")


    # --------------------------------
    # 3. Load jobs dataset
    # --------------------------------
    jobs = pd.read_csv("data/jobs.csv")


    # --------------------------------
    # 4. Select a job
    # --------------------------------
    st.subheader("📋 Resume Evaluation")

    job_title = st.selectbox(
        "Select a Job",
        jobs["job_title"].unique()
    )


    # --------------------------------
    # 5. Get selected job
    # --------------------------------
    selected_job = jobs[
        jobs["job_title"] == job_title
    ].iloc[0]


    # --------------------------------
    # 6. Required skills
    # --------------------------------
    required_skills = [
        skill.strip()
        for skill in selected_job["skills"].split(",")
    ]


    # --------------------------------
    # 7. Calculate score
    # --------------------------------
    score = calculate_resume_score(
        skills,
        required_skills
    )


    # --------------------------------
# 8. Resume Score
# --------------------------------

st.subheader("📊 Resume Score")

st.markdown(
    f"""
    <div style="display:flex; justify-content:center; margin:20px;">
        <div style="
            width:220px;
            height:220px;
            border-radius:50%;
            background:conic-gradient(
                #4CAF50 {score}%,
                #e0e0e0 {score}% 100%
            );
            display:flex;
            align-items:center;
            justify-content:center;
        ">
            <div style="
                width:150px;
                height:150px;
                border-radius:50%;
                background:white;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:32px;
                font-weight:bold;
            ">
                {score}%
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(f"✅ Matched Skills: {score}%")
st.write(f"⚠️ Missing Skills: {100 - score}%")


    # --------------------------------
    # 9. Missing Skills
    # --------------------------------
    missing_skills = get_missing_skills(
        skills,
        required_skills
    )

    st.subheader("⚠️ Missing Skills")

    if missing_skills:

        for skill in missing_skills:
            st.warning(skill)

    else:

        st.success(
            "🎉 You have all the required skills!"
        )


    # --------------------------------
    # 10. Job Recommendations
    # --------------------------------
    st.subheader("🎯 Recommended Jobs")

    recommendations = recommend_jobs(
        text,
        jobs,
        top_n=5
    )


    # --------------------------------
    # 11. Display recommendations
    # --------------------------------
    for _, job in recommendations.iterrows():

        st.write(
            f"### 💼 {job['job_title']}"
        )

        st.write(
            f"**Company:** {job['company']}"
        )

        st.write(
            f"**Location:** {job['location']}"
        )

        st.write(
            f"**Match Score:** "
            f"**{job['match_score']}%**"
        )

        st.progress(
            min(int(job["match_score"]), 100)
        )

        st.write("---")

