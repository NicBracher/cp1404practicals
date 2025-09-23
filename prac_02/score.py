"""
CP1404/CP5632 - Practical 2 - Nicholas Bracher

Broken program to determine score status

EDIT 22/09/25: Addition of functions and random module to generate random score/grade to prac_01 broken_score.py
"""

import random


def main():
    """Get user score, use random module, and display grade for user and random score."""
    user_score = float(input("Enter score: "))
    user_grade = calculate_grade(user_score)
    print(f"User grade: {user_grade}")

    random_score = random.randint(0, 100)
    random_grade = calculate_grade(random_score)
    print(f"Random score: {random_score} \nGrade: {random_grade}")


def calculate_grade(score):
    """Calculate grade from given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score < 50:
        return "Bad"
    if score < 90:
        return "Pass"
    return "Excellent"


main()
