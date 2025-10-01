# Gamified Study & Learning Platform

#### Video Demo: https://youtu.be/XH7QPqBERUM
#### Description:This is my final project for Harvard’s CS50 course on edX: Gamified Study Platform. It’s a web app with flashcards, quizzes, gamification features, a CLI tool, Lua mini-game, and a Chrome extension to make learning more fun and interactive.This project was built as part of the CS50 final project requirement. Special thanks to the CS50 team and community for guidance and resources!

## Overview
The **Gamified Study & Learning Platform** is my CS50 Final Project. It is a cross-platform educational system designed to make studying fun by blending quizzes, flashcards, and gamification. Students can practice a variety of academic subjects, track their learning progress, and stay motivated by earning virtual coins and unlocking rewards.

The project is implemented as:
- A **web app** using Python (Flask), SQL, HTML, CSS, and Jinja templates.
- A **command-line tool** in C for quick quiz practice in the terminal.
- A **Chrome extension** written in JavaScript for “pop quizzes” directly inside the browser.

This project integrates **nine subjects** into one platform:
1. Mathematics
2. Geography
3. English Literature
4. Computer Science
5. Home Science
6. Sociology
7. Political Theory
8. Economics
9. Finance

By covering diverse areas of knowledge, students can build well-rounded skills while staying engaged through game-like elements.

---

## Features

### 1. Flashcards & Quizzes
- Students can select any subject and answer multiple-choice or short-answer quizzes.
- Quizzes are stored in a SQL database and dynamically displayed in the web interface.
- Input is case-insensitive and trims whitespace, ensuring answers are checked fairly.

### 2. Gamification
- Each correct answer earns **coins**.
- At milestones (5, 10 coins), students unlock avatars and achievements.
- Wrong answers are still logged in history but do not increase coin count.

### 3. Learning History
- Every quiz submission is stored with a **timestamp**.
- Students can review their progress day by day, week by week, and month by month.
- The `/history` page shows all attempts and scores, encouraging reflection and improvement.

### 4. Cross-Platform Access
- **Web App (Flask + SQL):** Full functionality, including subjects, quizzes, history, and profile/avatars.
- **Command-Line Tool (C):** Lightweight Q&A in terminal. Useful for quick study without opening the browser.
- **Chrome Extension (JavaScript):** Provides instant quizzes inside Chrome, motivating students to learn in spare moments.

---

## File Structure
Here is an explanation of each file included in this project:

- **app.py** → Main Flask application; handles routes for homepage, subjects, quizzes, history, and profile.
- **models.py** → SQLAlchemy models defining Subjects, Quizzes, and Progress tables.
- **requirements.txt** → Python dependencies (`flask`, `flask_sqlalchemy`).
- **templates/layout.html** → Base HTML layout with navigation.
- **templates/index.html** → Homepage listing all subjects.
- **templates/subjects.html** → Displays quizzes under a selected subject.
- **templates/quiz.html** → Quiz page where students answer questions and submit results.
- **templates/history.html** → Displays student history (quiz scores and timestamps).
- **templates/profile.html** → Shows current coin count and unlocked avatars.
- **static/styles.css** → Styling for the web app.
- **seed_data.py** → Script for inserting 9 subjects and 30 sample quizzes into the database.
- **cli_tool.c** → Command-line quiz program written in C.
- **chrome_extension/** → Folder containing `manifest.json`, `popup.html`, `popup.js` for the extension.

---

## How It Works

1. **Setup the database**
   ```bash
   pip install -r requirements.txt
   flask shell
   >>> from models import db
   >>> db.create_all()
   >>> exit()
   python seed_data.py


Design Choices

I debated between limiting the project to a single platform or expanding it across multiple environments. I chose a cross-platform approach because:

Students study in different contexts (desktop, mobile, quick breaks).

A web app alone might feel too static. Adding CLI + extension creates more flexibility.

Gamification (coins, avatars) is easier to demonstrate when multiple touchpoints are available.

I also used SQLite for simplicity (no external DB setup required) and Flask because it integrates smoothly with Python and CS50’s environment. For the command-line component, I chose C to showcase lower-level programming skills from earlier in the course.


Example Tests

Here are sample test cases I used while developing:

Math → 2+2=4 (correct).

Geography → Capital of France = Paris (correct).

Sociology → “Study of society” (correct).

Finance → “Time value of money” (explain concept).

English Literature → Identify Shakespeare play from quote.

A total of 30 sample quizzes across 9 subjects are seeded in the database.

Future Improvements

Build a mobile app using Swift/Java for flashcards on the go.

Add leaderboards and multiplayer quiz challenges.

More advanced progress analytics (graphs, charts).

Support importing/exporting quiz sets for teachers and students.

Conclusion

The Gamified Study & Learning Platform combines learning and fun in a single cross-platform solution. Students can practice across multiple subjects, earn rewards, and monitor their improvement. This project demonstrates skills in Python, SQL, C, and JavaScript, along with web development, database design, and user interface creation.

CS50 was truly an incredible journey, and I am proud to submit this as my final project.


Credits

Built as the final project for CS50x.
Developed by Caroline Mildred Gomes
GitHub: carolinemildredgomes-hub
edX: CM_2508_CC10
Location: Dhaka, Bangladesh
Date: 1/10/2025
