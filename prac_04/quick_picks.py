"""
CP1404/CP5632 - Practical 4 - Nicholas Bracher
Program to generate quick picks for a lottery
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45


def main():
    """Use user input to generate quick pick numbers within given range for lottery."""
    number_of_quick_picks = get_valid_number("How many quick picks? ", 0)
    for i in range(number_of_quick_picks):
        quick_pick_numbers = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            while number in quick_pick_numbers:
                number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            quick_pick_numbers.append(number)
            quick_pick_numbers.sort()
        print(" ".join(f"{number:2}" for number in quick_pick_numbers))


def get_valid_number(prompt, low):
    """Get a valid number from the user."""
    number = int(input(prompt))
    while number < low:
        print(f"Invalid score. Please enter a number above {low}.")
        number = int(input(prompt))
    return number


main()
