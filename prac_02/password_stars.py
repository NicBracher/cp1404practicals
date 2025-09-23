"""
CP1404/CP5632 - Practical 2 - Nicholas Bracher

Take user password and print asterisks in place of the characters
"""

MINIMUM_LENGTH = 6


def main():
    """Call functions to get a password and print stars."""
    password = get_valid_password()
    print_stars(password)


def get_valid_password():
    """Get a valid password from the user."""

    password = input(f"Enter password of atleast {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long.")
        password = input("Enter password: ")

    return password


def print_stars(password):
    """Print stars corresponding to the length of the password."""
    print("*" * len(password))


main()
