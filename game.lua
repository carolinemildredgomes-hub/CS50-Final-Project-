-- Simple text-based mini-game for Codespaces terminal
print("🎮 Welcome to the Study Reward Mini-Game!")

local score = 0

local quizzes = {
    {q = "2 + 2 = ?", a = "4"},
    {q = "Capital of France?", a = "Paris"},
    {q = "Binary of 5?", a = "101"},
    {q = "Author of Hamlet?", a = "Shakespeare"},
    {q = "Currency of Japan?", a = "Yen"}
}

for i, quiz in ipairs(quizzes) do
    io.write("Q" .. i .. ": " .. quiz.q .. " ")
    local answer = io.read()
    if string.lower(answer) == string.lower(quiz.a) then
        print("✅ Correct!")
        score = score + 1
    else
        print("❌ Wrong! Answer: " .. quiz.a)
    end
end

print("\n🎯 You answered " .. score .. " out of " .. #quizzes .. " correctly!")
print("💰 Coins earned: " .. score)
