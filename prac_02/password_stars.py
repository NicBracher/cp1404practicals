"""
CP1404/CP5632 - Practical - Nicholas Bracher
"""


def main():
    password = get_valid_password()
    print_stars(password)


def get_valid_password():
    """Get a valid password from the user."""
    minimum_length = 6

    password = input("Enter password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters long.")
        password = input("Enter password: ")

    return password


def print_stars(password):
    """Print stars corresponding to the length of the password."""
    print("*" * len(password))


main()
