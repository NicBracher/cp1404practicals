"""
CP1404/CP5632 - Practical 5 - Nicholas Bracher

Emails
Estimate: 40 minutes
Actual: 24 minutes

"""


def main():
    """Get email from user and confirm their name and store in a dictionary."""
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        suspected_name = extract_name(email)

        name_confirmation = input(
            f"Is your name {suspected_name}? (Y/n) ").upper()
        while name_confirmation not in ["", "Y", "N"]:
            print("Invalid input. Please enter Y or N.")
            name_confirmation = input(
                f"Is your name {suspected_name}? (Y/n) ").upper()

        if name_confirmation == "" or name_confirmation == "Y":
            email_to_name[email] = suspected_name
        else:
            name = input("Name: ")
            email_to_name[email] = name

        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from a given email address."""
    suspected_name = email.split("@")[0]
    if "." in suspected_name:
        suspected_name_parts = suspected_name.split(".")
        name = " ".join(suspected_name_parts).title()
    else:
        name = suspected_name.title()
    return name


main()
