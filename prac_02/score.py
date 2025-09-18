"""
CP1404/CP5632 - Practical - Nicholas Bracher
"""
import random


def main():
    user_score = float(input("Enter score: "))
    user_grade = calculate_grade(user_score)
    print(f"User grade: {user_grade}")

    random_score = random.randint(0, 100)
    random_grade = calculate_grade(random_score)
    print(f"Random score: {random_score} \nGrade: {random_grade}")


def calculate_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()
