# AI-Based Mock Interview System

## 📌 Project Overview
The **AI-Based Mock Interview System** is a web-based application developed using **Flask, Python, HTML, CSS, and JSON**.  
This system helps students and job seekers practice interview questions and receive **automated evaluation and feedback** based on their answers.

It simulates a basic interview environment and provides:
- interview questions
- answer evaluation
- score calculation
- AI-based feedback
- performance summary

---

## 🎯 Objectives
- To help users practice interview questions.
- To improve communication and technical answering skills.
- To provide instant score and feedback automatically.
- To simulate a simple AI-driven mock interview environment.

---

## 🚀 Features
- User-friendly web interface
- Candidate name and domain selection
- Multiple interview categories:
  - Python
  - HR
  - DBMS
- Question-by-question interview flow
- AI-based keyword matching evaluation
- Score calculation for each answer
- Instant feedback generation
- Final result summary
- Saves interview results into CSV file

---

## 🛠️ Technologies Used

### Frontend
- HTML
- CSS

### Backend
- Python
- Flask

### Data Storage
- JSON
- CSV

### AI / NLP Logic
- Keyword Matching
- Rule-Based Evaluation

---

## 📂 Project Structure

ai_mock_interview_flask/
│
├── app.py
├── questions.json
├── results.csv
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── interview.html
│   └── result.html
│
└── static/
    └── style.css

---

## ⚙️ Installation Steps

### 1. Clone or Download the Project
Download the project folder and open it in VS Code.

### 2. Install Required Libraries
Open terminal and run:

```bash
pip install -r requirements.txt
---
▶️ How It Works
User enters name
User selects interview domain
System displays interview questions one by one
User types answer
System checks answer using keyword-based AI logic
Score and feedback are generated
Final result is displayed
Result is saved in CSV file
---
file
🤖 How AI Is Used in This Project

This project uses a basic AI/NLP-based answer evaluation method.

The system:

compares the user answer with important keywords
checks relevance of the answer
gives score based on keyword match
generates automatic feedback

This creates a simple AI-assisted interview evaluation system.
---
📊 Modules of the Project
1. User Input Module

Collects candidate name and selected domain.

2. Question Display Module

Displays interview questions one by one.

3. Answer Evaluation Module

Checks answers using keyword matching logic.

4. Feedback Generation Module

Generates feedback based on answer quality.

5. Result Storage Module

Stores interview results in CSV file.
---
📈 Sample Output

At the end of the interview, the system shows:

Candidate Name
Interview Domain
Final Score
Percentage
AI Feedback
Answer Summary
---
📈 Sample Output

At the end of the interview, the system shows:

Candidate Name
Interview Domain
Final Score
Percentage
AI Feedback
Answer Summary
---
🔮 Future Enhancements
Voice-based interview system
Speech-to-text answer input
Face emotion detection
Resume-based question generation
Advanced NLP/LLM-based evaluation
Admin dashboard for performance tracking
---
✅ Conclusion

The AI-Based Mock Interview System is a simple and useful web application that helps users practice interview questions and improve their confidence.
It provides a basic AI-based evaluation system and can be further enhanced into a smart interview preparation platform.
---
👨‍💻 Developed By
HEMANTH KUMAR S J
---

---

# Small Important Fix

In your README, replace:

```md
**HEMANTH KUMAR S J**
---
