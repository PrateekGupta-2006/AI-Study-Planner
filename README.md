# AI Study Planner for Engineering Students 

## Problem Statement
Engineering students face a highly demanding academic environment with multiple complex subjects, varying cognitive loads, prerequisite dependencies, and tight deadlines. Traditional study planning tools such as static timetables or generic to do apps fail to adapt to subject difficulty, individual confidence levels, and dynamic priorities.

As a result, students often study hard but not smart.

## Solution
AI Study Planner is a **console-based, AI inspired study planning system** designed specifically for engineering students. It intelligently allocates study time across subjects based on credits, weak areas, self rated confidence levels, and available study hours.

The system generates:
- Subject wise study hour allocation
- A weekly study plan
- Actionable insights to guide what to study, when, and why

This ensures balanced learning, reduced stress, and improved conceptual understanding.

## Key Features
- Personalized study planning for engineering students
- Confidence aware subject prioritization
- Cognitive load balancing (deep study vs revision)
- Actionable insights instead of static schedules
- Lightweight and easy to run working prototype

## AI Logic (How It Works)
Each subject is assigned a **Priority Score** using the following formula:

Priority Score =  
(Credits × 0.4) + ((5 − Confidence Level) × 0.4) + (Number of Weak Topics × 0.2)

Study hours are allocated proportionally based on this priority score.

### Smart Scheduling Rules:
- Subjects with **low confidence and more weak topics** are prioritized first
- Strong subjects receive **lighter revision focused schedules**
- Weekly study hours are balanced across all subjects

## Sample Output
- Subject wise study hour allocation (per week)
- Weekly study plan (Monday to Sunday)
- Actionable insights such as:
  - “Focus early on Operating Systems due to low confidence”
  - “Reduce over studying for strong subjects”
- Outcome-oriented summary including expected confidence improvement

  
## Tech Stack
- Python
- Rule based AI prioritization logic
- Console based execution (no external dependencies)

---

## Demo Video
🎥 Demo Video Link: https://drive.google.com/file/d/1TwXqoXoakVP6kpTwWTNbBkpQYL9RulwA/view?usp=sharing

The demo video shows:
- Program execution
- Generated study plan
- Explanation of AI logic and impact

---

## How to Run the Project
1. Ensure Python is installed
2. Clone the repository
3. Run the following command:

```bash
python app.py
