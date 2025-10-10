"""
CP1404/CP5632 - Practical 4 - Nicholas Bracher
Basic list exercise program 
"""


def main():
    """Maain body of the program that will get use input and call functions."""
    numbers = []
    usernames = [
        "jimbo",
        "giltson98",
        "derekf",
        "WhatSup",
        "NicolEye",
        "swei45",
        "BaseInterpreterInterface",
        "BaseStdIn",
        "Command",
        "ExecState",
        "InteractiveConsole",
        "InterpreterInterface",
        "StartServer",
        "bob",
    ]

    for i in range(5):
        number = int(input("number: "))
        numbers.append(number)
    display_numbers_info(numbers)

    username = input("Input your username: ")
    access = validate_username(usernames, username)
    print(access)


def display_numbers_info(numbers):
    """Display information from the numbers list."""
    print(
        f"The first number is {numbers[0]}\n"
        f"The last number is {numbers[-1]}\n"
        f"The smallest number is {min(numbers)}\n"
        f"The largest number is {max(numbers)}\n"
        f"The average of the numbers is {sum(numbers) / len(numbers):.1f}"
    )


def validate_username(usernames, username):
    """Validate username against list of given usernames."""
    for name in usernames:
        if username == name:
            return "Access granted"
        return "Access denied"


main()
