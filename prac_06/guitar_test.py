"""
CP1404/CP5632 Practical - Nicolas Bracher
Time estimate: 45 minutes
Time actual:

"""

from guitar import Guitar

# guitar_one = Guitar("Gibson L-5 CES", 1925, 16000)
# guitar_two = Guitar("Another Guitar", 2013, 500)

# print(f"{guitar_one.name} get_age() - Expected 100. Got {guitar_one.get_age()}")
# print(f"{guitar_two.name} get_age() - Expected 12. Got {guitar_two.get_age()}")

# print(f"{guitar_one.name} is_vintage() - Expected True. Got {guitar_one.is_vintage()}")
# print(f"{guitar_two.name} is_vintage() - Expected False. Got {guitar_two.is_vintage()}")


def main():
    guitars = get_user_input()
    display_guitars(guitars)


def get_user_input():
    """Get guitar details from user without error checking."""
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")

    # Test data:
    # guitars.append(Guitar("Gibson L-5 CES", 1925, 16000))
    # guitars.append(Guitar("Another Guitar", 2013, 500))
    # guitars.append(Guitar("Yet Another", 1990, 1500))
    # guitars.append(Guitar("This is one as well", 1970, 3000))
    # guitars.append(Guitar("Can't forget about this one", 2020, 800))
    # guitars.append(Guitar("Not a guitar?", 1950, 12000))
    # guitars.append(Guitar("JK, it was a guitar", 2005, 2000))

    return guitars


def display_guitars(guitars):
    """Display guitar details."""
    print("These are my guitars:")

    name_column_width = max(len(guitar.name) for guitar in guitars)
    cost_column_width = max(len(f"{guitar.cost:.2f}") for guitar in guitars)

    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>{name_column_width}} ({guitar.year}), worth $ {guitar.cost:{cost_column_width},.2f}{vintage_string}"
        )

        

main()
