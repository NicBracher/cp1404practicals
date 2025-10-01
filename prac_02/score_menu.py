"""
CP1404/CP5632 - Practical 2 - Nicholas Bracher

Menu driven program that uses functions to take a user input, determine and output corresponding grade.
"""

MENU = "\n(G)et valid score\n(P)rint grade result\n(S)how stars\n(Q)uit\n"


def main():
    """Control main body through menu driven user interaction and fucntion calls."""

    user_score = None
    choice = get_menu_selection(
        f"Welcome to the score menu! \nPlease choose from the below options: \n{MENU}"
    )

    while choice != "Q":

        if choice == "G":
            user_score = get_valid_score("\nEnter score: ", 0, 100)
            print(f"\n-> Score {user_score} recorded.")
            choice = get_menu_selection(MENU)

        elif choice == "P":
            if user_score == None:
                choice = get_menu_selection(
                    "Please input your score first. \n")
            else:
                grade = calculate_grade(user_score)
                print(f"\n-> Score: {user_score} \n-> Grade: {grade}")
                choice = get_menu_selection(MENU)

        elif choice == "S":
            if user_score == None:
                choice = get_menu_selection(
                    "Please input your score first. \n")
            else:
                print("*" * user_score)
                choice = get_menu_selection(MENU)

    print("Thank you for using the score menu. Goodbye!")


def get_menu_selection(prompt):
    """Get a valid menu selection input from the user."""
    print(prompt)
    choice = choice = input(">>> ").upper()

    while choice != "Q" and choice != "G" and choice != "P" and choice != "S":
        print(f"\nInvalid choice. Please choose between: \n{MENU}")
        choice = input(">>> ").upper()
    return choice


def get_valid_score(prompt, low, high):
    """Get a valid score from the user."""
    score = int(input(prompt))

    while score < low or score > high:
        print(f"Invalid score. Please enter a score between {low} and {high}.")
        score = int(input(prompt))
    return score


def calculate_grade(score):
    """Calculate grade from given score."""
    if score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    return "Excellent"


main()
