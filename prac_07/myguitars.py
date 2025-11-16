"""
CP1404 Practical 7 - My Guitars
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = load_file_contents(FILENAME)
    new_guitars = get_user_input()
    guitars += new_guitars   
    guitars.sort()
    write_to_file(FILENAME, guitars)
    display_guitars(guitars)


def load_file_contents(filename):
    """Process guitar file and display vintage status."""
    in_file = open(filename, 'r')
    guitars = []
    for line in in_file:
        parts = line.strip().split(',')
        name, year, cost = parts
        guitar = Guitar(name, int(year), float(cost))
        guitars.append(guitar)
    in_file.close()
    return guitars


def display_guitars(guitars):
    """Display guitars and their corresponding information."""
    for guitar in guitars:
        print(guitar)


def get_user_input():
    "Get user input and return it as a string."
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")
    return guitars


def write_to_file(filename, guitars):
    out_file = open(filename, 'w')
    lines = [f"{guitar.name},{guitar.year},{guitar.cost}\n" for guitar in guitars]
    out_file.writelines(lines)
    out_file.close()
    return


if __name__ == "__main__":
    main()
