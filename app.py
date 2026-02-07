# AI Study Planner for Engineering Students

from datetime import date

print("AI STUDY PLANNER FOR ENGINEERING STUDENTS")
print("=" * 50)

# ================= STUDENT DETAILS =================
student = {
    "name": "Aman",
    "college": "XYZ Institute of Technology",
    "branch": "Computer Science Engineering",
    "graduation_year": "2026",
    "email": "aman@example.com"
}

# ================= SUBJECT DETAILS =================
subjects = [
    {
        "name": "Data Structures",
        "credits": 4,
        "weak_topics": ["Trees", "Graphs"],
        "confidence": 3
    },
    {
        "name": "Operating Systems",
        "credits": 3,
        "weak_topics": ["Deadlocks", "Memory Management"],
        "confidence": 2
    },
    {
        "name": "Engineering Mathematics",
        "credits": 4,
        "weak_topics": ["Laplace Transform"],
        "confidence": 3
    }
]

# ================= STUDY AVAILABILITY =================
weekday_hours = 3
weekend_hours = 6
preferred_time = "Night"
target_completion_date = date(2026, 3, 15)

# ================= AI PRIORITIZATION LOGIC =================
print("\nCalculating AI-based priorities...\n")

total_weekly_hours = weekday_hours * 5 + weekend_hours * 2

total_priority_score = 0
for subject in subjects:
    priority_score = (
        subject["credits"] * 0.4 +
        (5 - subject["confidence"]) * 0.4 +
        len(subject["weak_topics"]) * 0.2
    )
    subject["priority_score"] = round(priority_score, 2)
    total_priority_score += priority_score

# Allocate hours
for subject in subjects:
    subject["allocated_hours"] = round(
        (subject["priority_score"] / total_priority_score) * total_weekly_hours, 2
    )

# Sort subjects by priority
subjects.sort(key=lambda x: x["priority_score"], reverse=True)

# ================= OUTPUT =================
print("SUBJECT-WISE STUDY ALLOCATION (PER WEEK)")
print("-" * 50)

for subject in subjects:
    print(f"""
Subject: {subject['name']}
Credits: {subject['credits']}
Confidence Level: {subject['confidence']}/5
Weak Topics: {', '.join(subject['weak_topics'])}
Allocated Study Hours: {subject['allocated_hours']} hrs/week
""")

# ================= WEEKLY STUDY PLAN =================
print("\nWEEKLY STUDY PLAN")
print("-" * 50)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i, day in enumerate(days):
    subject = subjects[i % len(subjects)]
    focus = "Weak Topics & Practice" if subject["confidence"] <= 3 else "Revision"
    print(f"{day}: {subject['name']} ({focus}) – {preferred_time}")

# ================= ACTIONABLE INSIGHTS =================
print("\nACTIONABLE INSIGHTS")
print("-" * 50)

for subject in subjects:
    if subject["confidence"] <= 2:
        print(f"- Focus early on {subject['name']} due to low confidence.")
    elif subject["confidence"] >= 4:
        print(f"- Reduce over-studying for {subject['name']} and focus on revision.")

# ================= NEXT 7 DAYS =================
print("\nNEXT 7 DAYS FOCUS")
print("-" * 50)

for subject in subjects[:2]:
    print(f"- Prioritize weak topics in {subject['name']}")

# ================= SUMMARY =================
print("\nOUTCOME SUMMARY")
print("-" * 50)
print(f"Target Completion Date: {target_completion_date}")
print(f"Total Weekly Study Hours: {total_weekly_hours} hrs")
print("Expected Confidence Improvement: +1 to +2 levels")
print("Reduced Last-Minute Stress: YES")

print("\nAI Study Plan Generated Successfully!")
