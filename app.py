
import streamlit as st

# Page settings
st.set_page_config(
    page_title="CareerAI Dashboard",
    page_icon="💼",
    layout="wide"
)

# Title
st.title(" CareerAI Dashboard")
st.write("AI-powered career guidance for students and freshers.")

# User details
st.subheader("Enter Your Details")

name = st.text_input("Name")

skills = st.text_input(
    "Skills",
    placeholder="Python, SQL, Excel, Machine Learning"
)

education = st.selectbox(
    "Education",
    ["MCA", "B.Tech", "BCA", "M.Tech", "Other"]
)

experience = st.selectbox(
    "Experience",
    ["Fresher", "0-1 Year", "1-2 Years", "2+ Years"]
)

# Recommendation button
if st.button(" Get Career Recommendation"):

    if name and skills:

        skill_text = skills.lower()

        recommendations = []
        detected_skills = []

        # Detect skills
        if "python" in skill_text:
            recommendations.append("Python Developer")
            detected_skills.append("Python")

        if "sql" in skill_text:
            recommendations.append("SQL Developer")
            detected_skills.append("SQL")

        if "excel" in skill_text:
            recommendations.append("Data Analyst")
            detected_skills.append("Excel")

        if "machine learning" in skill_text or "ml" in skill_text:
            recommendations.append("Data Scientist")
            detected_skills.append("Machine Learning")

        if "power bi" in skill_text:
            recommendations.append("Power BI / Data Analyst")
            detected_skills.append("Power BI")

        if "nlp" in skill_text:
            recommendations.append("NLP / AI Engineer")
            detected_skills.append("NLP")

        if not recommendations:
            recommendations.append("Data Analyst")

        # Skills Match Score
        total_skills = 6

        match_score = min(
            int((len(detected_skills) / total_skills) * 100),
            100
        )

        # Success message
        st.success(
            f"Hello {name}! Your CareerAI analysis is ready."
        )

        # Skills score
        st.subheader(" Skills Match Score")

        st.progress(match_score / 100)

        st.write(f"**{match_score}% Skills Match**")

        # Detected skills
        if detected_skills:
            st.write(
                "**Detected Skills:** "
                + ", ".join(detected_skills)
            )

        # Career recommendations
        st.subheader(" Recommended Career Roles")

        for role in recommendations:
            st.write( role)

        # Skill Gap Analysis
        st.subheader(" Recommended Skills to Learn")

        skill_gaps = []

        if "power bi" not in skill_text:
            skill_gaps.append("Power BI")

        if "statistics" not in skill_text:
            skill_gaps.append("Statistics")

        if "deep learning" not in skill_text:
            skill_gaps.append("Deep Learning")

        if "nlp" not in skill_text:
            skill_gaps.append("NLP")

        if "generative ai" not in skill_text and "genai" not in skill_text:
            skill_gaps.append("Generative AI")

        for skill in skill_gaps:
            st.write( skill)

        # Career Summary
        st.subheader(" Career Summary")

        detected_text = ", ".join(detected_skills)

        st.write(
            f"You have a foundation in {detected_text}. "
            f"As a {experience.lower()} with {education}, "
            "you can explore entry-level technology and data-related roles."
        )

        # Education and experience
        st.info(
            f"Your education: {education} | "
            f"Experience: {experience}"
        )

    else:
        st.warning("Please enter your name and skills.")
