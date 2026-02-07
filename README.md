# AI Study Planner for Engineering Students 🤖📘

## Problem
Engineering students struggle to balance multiple complex subjects with varying difficulty levels, prerequisites, and deadlines. Traditional planners are static and fail to adapt to confidence levels and cognitive load.

## Solution
AI Study Planner is an adaptive, personalized planning system that intelligently allocates study time based on subject credits, self-rated confidence, weak topics, and available hours.

## Key Features
- Personalized weekly study schedule
- Confidence-aware subject prioritization
- Cognitive load balancing
- Actionable study insights
- Dynamic time allocation

## AI Logic
Each subject is assigned a Priority Score using:

Priority Score =
(Credits × 0.4) + ((5 − Confidence) × 0.4) + (Weak Topics × 0.2)

Study hours are distributed proportionally based on this score.

## Tech Stack
- Python
- Streamlit
- Pandas

## Demo Video
🎥 Demo Link: (Add your screen recording here)

## Impact
- Reduces last-minute cramming
- Improves deep conceptual understanding
- Helps students study smarter, not harder

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
