from models import db, Subject, Quiz
from app import app

subjects = ["Math","Geography","English Literature","Computer Science","Home Science","Sociology","Political Theory","Economics","Finance"]

quizzes = {
    "Math":[("2+2=?","4"),("Square root of 16?","4"),("5*6=?","30")],
    "Geography":[("Capital of France?","Paris"),("Largest continent?","Asia"),("River through Egypt?","Nile")],
    "English Literature":[("Author of Hamlet?","Shakespeare"),("Rhyme scheme of a sonnet?","ababcdcdefefgg"),("Who wrote 1984?","George Orwell")],
    "Computer Science":[("Binary of 5?","101"),("What is an algorithm?","Step by step instructions"),("SQL full form?","Structured Query Language")],
    "Home Science":[("Main nutrient in rice?","Carbohydrate"),("Vitamin for bones?","Vitamin D"),("Ideal temperature to store milk?","4°C")],
    "Sociology":[("Founder of Sociology?","Auguste Comte"),("Karl Marx theory?","Conflict theory"),("Social institution for education?","School")],
    "Political Theory":[("Who wrote The Republic?","Plato"),("Father of liberalism?","John Locke"),("Democracy means?","Rule by the people")],
    "Economics":[("Law of demand: when price rises, demand?","Falls"),("GDP full form?","Gross Domestic Product"),("Father of Economics?","Adam Smith")],
    "Finance":[("ROI stands for?","Return on Investment"),("Stock vs Bond: which is debt?","Bond"),("Currency of Japan?","Yen")]
}

with app.app_context():
    db.drop_all()
    db.create_all()
    for s in subjects:
        subj = Subject(name=s)
        db.session.add(subj)
        db.session.commit()
        for q,a in quizzes[s]:
            db.session.add(Quiz(subject_id=subj.id, question=q, answer=a))
    db.session.commit()
print("✅ Database populated.")
