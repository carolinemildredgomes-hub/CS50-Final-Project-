const quizzes=[
{question:"2 + 2 = ?",answer:"4"},
{question:"Capital of France?",answer:"Paris"},
{question:"Binary of 5?",answer:"101"},
{question:"Author of Hamlet?",answer:"Shakespeare"},
{question:"Currency of Japan?",answer:"Yen"}];
const randomQuiz=quizzes[Math.floor(Math.random()*quizzes.length)];
document.getElementById("question").innerText=randomQuiz.question;
function checkAnswer(){
const user=document.getElementById("answer").value.trim().toLowerCase();
const correct=randomQuiz.answer.toLowerCase();
document.getElementById("result").innerText=(user===correct)?"✅ Correct!":`❌ Wrong! Answer: ${randomQuiz.answer}`;
}
