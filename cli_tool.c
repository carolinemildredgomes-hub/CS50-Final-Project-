#include <stdio.h>
#include <string.h>

int main() {
    int score = 0;
    char answer[50];

    // Question 1
    printf("Q1: What is 2 + 2? ");
    scanf("%s", answer);
    if(strcmp(answer, "4") == 0) {
        printf("✅ Correct!\n");
        score++;
    } else {
        printf("❌ Wrong! Correct answer: 4\n");
    }

    // Question 2
    printf("Q2: Capital of France? ");
    scanf("%s", answer);
    if(strcasecmp(answer, "Paris") == 0) {
        printf("✅ Correct!\n");
        score++;
    } else {
        printf("❌ Wrong! Correct answer: Paris\n");
    }

    // Question 3
    printf("Q3: Binary of 5? ");
    scanf("%s", answer);
    if(strcmp(answer, "101") == 0) {
        printf("✅ Correct!\n");
        score++;
    } else {
        printf("❌ Wrong! Correct answer: 101\n");
    }

    // Final Score
    printf("\n🎯 You answered %d out of 3 questions correctly.\n", score);
    printf("💰 Coins earned: %d\n", score);  // 1 coin per correct answer

    return 0;
}

