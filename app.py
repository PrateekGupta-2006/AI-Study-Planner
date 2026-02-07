import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="AI Study Planner", layout="wide")

st.title("📘 AI Study Planner for Engineering Students")
st.caption("An AI-powered, adaptive study planner for engineering students")

# ---------------- STUDENT DETAILS ----------------
st.header("👤 Student Details")
name = st.text_input("Name")
college = st.text_input("College")
branch = st.text_input("Branch")
grad_year = st.text_input("Graduation Year")
email = st.text_input("Email ID")

# ---------------- SUBJECT INPUT ----------------
st.header("📚 Subjects")

num_subjects = st.number_input("Number of Subjects", 1, 6, 3)
subjects = []

for i in range(num_subjects):
    st.subheader(f"Subject {i+1}")
    subject = st.text_input("Subject Name", key=f"s{i}")
    credits = st.number_input("Credits", 1, 5, 3, key=f"c{i}")
    weak = st.text_input("Weak Topics (comma separated)", key=f"w{i}")
    confidence = st.slider("Confidence Level (1 = Low, 5 = High)", 1, 5, 3, key=f"conf{i}")

    subjects.append({
        "Subject": subject,
        "Credits": credits,
        "WeakTopics": weak,
        "Confidence": confidence
    })

# ---------------- STUDY TIME ----------------
st.header("⏰ Study Availability")
weekday = st.number_input("Weekday Study Hours (per day)", 1, 8, 3)
weekend = st.number_input("Weekend Study Hours (per day)", 1, 12, 6)
preferred_time = st.selectbox("Preferred Study Time", ["Morning", "Afternoon", "Night"])
target_date = st.date_input("Target Completion Date")

# ---------------- GENERATE PLAN ----------------
if st.button("🚀 Generate AI Study Plan"):
    df = pd.DataFrame(subjects)
    df["WeakCount"] = df["WeakTopics"].apply(lambda x: len(x.split(",")) if x else 0)

    # AI Priority Formula
    df["PriorityScore"] = (
        df["Credits"] * 0.4 +
        (5 - df["Confidence"]) * 0.4 +
        df["WeakCount"] * 0.2
    )

    total_score = df["PriorityScore"].sum()
    weekly_hours = weekday * 5 + weekend * 2
    df["AllocatedHours"] = (df["PriorityScore"] / total_score) * weekly_hours
    df = df.sort_values(by="PriorityScore", ascending=False)

    st.header("📊 Subject-wise Allocation")
    st.dataframe(df[["Subject", "Credits", "Confidence", "AllocatedHours"]])

    # ---------------- WEEKLY PLAN ----------------
    st.header("📆 Weekly Study Plan")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    schedule = []

    for i, day in enumerate(days):
        subject = df.iloc[i % len(df)]
        schedule.append({
            "Day": day,
            "Subject": subject["Subject"],
            "Focus": "Weak Topics & Practice" if subject["Confidence"] <= 3 else "Revision",
            "Study Time": preferred_time
        })

    st.table(pd.DataFrame(schedule))

    # ---------------- INSIGHTS ----------------
    st.header("✅ Actionable Insights")
    for _, row in df.iterrows():
        if row["Confidence"] <= 2:
            st.warning(f"Focus early on **{row['Subject']}** due to low confidence.")
        elif row["Confidence"] >= 4:
            st.success(f"Reduce load for **{row['Subject']}** to avoid over-studying.")

    # ---------------- NEXT STEPS ----------------
    st.header("📍 Next 7 Days Focus")
    for _, row in df.head(2).iterrows():
        st.info(f"Work on weak areas of **{row['Subject']}** first.")

    # ---------------- SUMMARY ----------------
    st.header("🎯 Outcome Summary")
    st.markdown(f"""
    - Target Completion Date: **{target_date}**
    - Weekly Study Hours: **{weekly_hours} hrs**
    - Expected Confidence Improvement: **+1 to +2 levels**
    - Reduced Last-Minute Stress: **Yes**
    """)

    st.success("AI Study Plan Generated Successfully 🎉")
