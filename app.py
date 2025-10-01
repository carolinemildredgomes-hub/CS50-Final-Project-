from flask import Flask, render_template, request, redirect
from models import db, Subject, Quiz, Progress
import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///study.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    subjects = Subject.query.all()
    return render_template("index.html", subjects=subjects)

@app.route("/subject/<int:subject_id>")
def subject(subject_id):
    subject = Subject.query.get(subject_id)
    quizzes = Quiz.query.filter_by(subject_id=subject_id).all()
    return render_template("subjects.html", subject=subject, quizzes=quizzes)

@app.route("/quiz/<int:quiz_id>", methods=["GET","POST"])
def quiz(quiz_id):
    quiz = Quiz.query.get(quiz_id)
    if request.method == "POST":
        answer = request.form["answer"]
        score = 100 if answer.strip().lower() == quiz.answer.lower() else 0
        progress = Progress(quiz_id=quiz_id, score=score, timestamp=datetime.datetime.now())
        db.session.add(progress)
        db.session.commit()
        return redirect("/history")
    return render_template("quiz.html", quiz=quiz)

@app.route("/history")
def history():
    progress = Progress.query.all()
    return render_template("history.html", progress=progress)

@app.route("/profile")
def profile():
    coins = sum([p.score for p in Progress.query.all()]) // 100
    return render_template("profile.html", coins=coins)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/game")
def game():
    return render_template("game.html")
