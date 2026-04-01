from flask import Flask, render_template, request, redirect, session, url_for
import json
import pandas as pd
import os

app = Flask(__name__)
app.secret_key = "mock_interview_secret_key"

# -----------------------------
# Load Questions
# -----------------------------
with open("questions.json", "r") as file:
    question_data = json.load(file)

# -----------------------------
# Home Page
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        domain = request.form["domain"]

        if name.strip() == "":
            return render_template("index.html", domains=question_data.keys(), error="Please enter your name.")

        session["name"] = name
        session["domain"] = domain
        session["current_question"] = 0
        session["score"] = 0
        session["answers"] = []

        return redirect(url_for("interview"))

    return render_template("index.html", domains=question_data.keys())

# -----------------------------
# Interview Page
# -----------------------------
@app.route("/interview", methods=["GET", "POST"])
def interview():
    if "name" not in session:
        return redirect(url_for("index"))

    domain = session["domain"]
    questions = question_data[domain]
    current_question = session["current_question"]

    if request.method == "POST":
        answer = request.form["answer"].strip()

        if answer == "":
            return render_template(
                "interview.html",
                question=questions[current_question]["question"],
                q_no=current_question + 1,
                total=len(questions),
                error="Please type your answer."
            )

        current_q = questions[current_question]
        keywords = current_q["keywords"]
        answer_lower = answer.lower()

        matched = sum(1 for word in keywords if word in answer_lower)
        question_score = matched * 2

        if matched >= 3:
            feedback = "Very good answer."
        elif matched >= 2:
            feedback = "Good answer, but can be improved."
        else:
            feedback = "Answer needs more relevant points."

        session["score"] += question_score

        answers = session["answers"]
        answers.append({
            "question": current_q["question"],
            "answer": answer,
            "score": question_score,
            "feedback": feedback
        })
        session["answers"] = answers

        session["current_question"] += 1

        if session["current_question"] >= len(questions):
            return redirect(url_for("result"))

        return redirect(url_for("interview"))

    return render_template(
        "interview.html",
        question=questions[current_question]["question"],
        q_no=current_question + 1,
        total=len(questions)
    )

# -----------------------------
# Result Page
# -----------------------------
@app.route("/result")
def result():
    if "name" not in session:
        return redirect(url_for("index"))

    name = session["name"]
    domain = session["domain"]
    score = session["score"]
    answers = session["answers"]

    total_questions = len(question_data[domain])
    max_score = total_questions * 8
    percentage = round((score / max_score) * 100, 2)

    if percentage >= 75:
        final_feedback = "Excellent performance! You are interview ready."
    elif percentage >= 50:
        final_feedback = "Good job! You have decent interview skills."
    else:
        final_feedback = "Needs improvement. Practice more."

    # Save to CSV
    result_data = {
        "Name": [name],
        "Domain": [domain],
        "Score": [score],
        "Percentage": [percentage],
        "Feedback": [final_feedback]
    }

    new_result = pd.DataFrame(result_data)

    if os.path.exists("results.csv"):
        existing = pd.read_csv("results.csv")
        updated = pd.concat([existing, new_result], ignore_index=True)
        updated.to_csv("results.csv", index=False)
    else:
        new_result.to_csv("results.csv", index=False)

    return render_template(
        "result.html",
        name=name,
        domain=domain,
        score=score,
        max_score=max_score,
        percentage=percentage,
        final_feedback=final_feedback,
        answers=answers
    )

# -----------------------------
# Restart
# -----------------------------
@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
