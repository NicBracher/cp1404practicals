"""
CP1404 Practical 7 - My Guitars
"""

from guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = process_file(FILENAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def process_file(filename):
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

if __name__ == "__main__":
    main()