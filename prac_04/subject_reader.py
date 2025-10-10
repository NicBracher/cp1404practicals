"""
CP1404/CP5632 - Practical 4 - Nicholas Bracher
Program to read subject data from a file and display it
"""

FILENAME = "subject_data.txt"


def main():
    """Control main body of program through function calls."""
    subjects = load_data(FILENAME)
    display_subject_details(subjects)


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subjects = []
    for line in input_file:
        parts = line.strip().split(',')
        parts[2] = int(parts[2])
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """Display details from subject list."""
    for details in subjects:
        print(
            f"{details[0]} is taught by {details[1]:<12} and has {details[2]:3} students")


main()
