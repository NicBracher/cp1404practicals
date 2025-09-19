"""
CP1404/CP5632 - Practical - Nicholas Bracher
"""

MENU = "\n(G)et valid score\n(P)rint grade result\n(S)how stars\n(Q)uit\n"


def main():
    user_score = 0

    print(
        f"Welcome to the score menu! \nPlease choose from the below options: \n{MENU}"
    )
    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "G":
            user_score = get_valid_input("\nEnter score: ")
            print(f"Score {user_score} recorded.")

            print(MENU)
            choice = input(">>> ").upper()

        elif choice == "P":
            grade = calculate_grade(user_score)
            print(f"\n-> Score: {user_score} \n-> Grade: {grade}\n")

            print(MENU)
            choice = input(">>> ").upper()

        elif choice == "S":
            print("*" * user_score)

            print(MENU)
            choice = input(">>> ").upper()

        else:
            print(f"\nInvalid choice. Please choose between: \n{MENU}")
            choice = input(">>> ").upper()

    print("Thank you for using the score menu. Goodbye!")


def get_valid_input(prompt):
    """Get a valid score from the user."""
    score_value = int(input(prompt))

    while score_value < 0 or score_value > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score_value = int(input(prompt))

    return score_value


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
