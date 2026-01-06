import streamlit as st
import pandas as pd

# -------------------- TITLE & DESCRIPTION --------------------
st.set_page_config(page_title="Skill Gap Analyzer", layout="wide")
st.title("Skill Gap Analyzer Dashboard")
st.write("Upload resume or job description to analyze skill gaps end-to-end.")

# -------------------- SIDEBAR --------------------
st.sidebar.title("Navigation")
st.sidebar.write("1. Upload Files")
st.sidebar.write("2. Analyze Skills")
st.sidebar.write("3. Visualize Results")
st.sidebar.write("4. Download Report")

# -------------------- SESSION STATE --------------------
if "uploaded_text" not in st.session_state:
    st.session_state.uploaded_text = ""

# -------------------- FILE UPLOADER --------------------
uploaded_file = st.file_uploader(
    "Upload Resume / Job Description",
    type=["pdf", "docx", "txt"]
)

# -------------------- FILE HANDLING --------------------
if uploaded_file:
    st.success(f"Uploaded File: {uploaded_file.name}")

    try:
        text = uploaded_file.read().decode("utf-8")
        st.session_state.uploaded_text = text

        st.text_area(
            "File Preview (First 300 Characters)",
            text[:300],
            height=150
        )

    except:
        st.error("Unsupported file or empty file!")

else:
    st.warning("Please upload a PDF, DOCX, or TXT file.")

# -------------------- PROCESS BUTTON --------------------
if st.button("Analyze Skills"):

    if st.session_state.uploaded_text == "":
        st.error("No data to process!")
    else:
        # -------------------- DUMMY SKILL LOGIC --------------------
        matched_skills = ["Python", "SQL", "Machine Learning"]
        missing_skills = ["Power BI", "Docker"]

        match_percentage = int(
            (len(matched_skills) /
            (len(matched_skills) + len(missing_skills))) * 100
        )

        # -------------------- METRIC --------------------
        st.metric("Skill Match Percentage", f"{match_percentage}%")

        # -------------------- SECTIONS --------------------
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Matched Skills")
            st.write(matched_skills)

        with col2:
            st.subheader("Missing Skills")
            st.write(missing_skills)

        # -------------------- BAR CHART --------------------
        chart_data = pd.DataFrame({
            "Category": ["Matched Skills", "Missing Skills"],
            "Count": [len(matched_skills), len(missing_skills)]
        })
        st.bar_chart(chart_data.set_index("Category"))

        # -------------------- TABLE --------------------
        skill_table = pd.DataFrame({
            "Skill": matched_skills + missing_skills,
            "Similarity Score": [0.92, 0.88, 0.80, 0.45, 0.30]
        })

        st.subheader("Skill Similarity Table")
        st.table(skill_table)

        # -------------------- DOWNLOAD CSV --------------------
        csv = skill_table.to_csv(index=False)
        st.download_button(
            label="Download Skill Gap Report (CSV)",
            data=csv,
            file_name="skill_gap_report.csv",
            mime="text/csv"
        )
