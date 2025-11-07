"""
CP1404 Practical 7 - Project Management

Time estimate: 75 minutes
Time actual: (10:25am)

This file contains the data for this exercise delimited by tabs.
The first line is a header, explaining the fields for each project.

Write a program in project_management.py to load and save a data file and use a list of Project objects.
Load projects from the default data file, projects.txt, when the program starts, before the menu.
When the user quits, give them the choice of saving to the default file.
Note that there are menu options for loading from and saving to different files.
Your program should contain a menu with the following options:

Load projects
(Prompt the user for a filename to load projects from and load them)
Save projects
(Prompt the user for a filename to save projects to and save them)
Display projects
(Display two groups: incomplete projects; completed projects, both sorted by priority)
Filter projects by date
(Ask the user for a date and display only projects that start after that date, sorted by date)
Add new project
(Ask the user for the inputs and add a new project to memory)
Update project
(Choose a project, then modify the completion % and/or priority - the user can leave either input blank to retain existing values)

You should notice that there are two different scenarios for both loading and saving.
Consider SRP and how you can write a single function for loading that you use in both scenarios: the default filename and the user-selected filename.

The following code reads a string from user input, converts it to a date object (using the strptime method from the datetime type), prints the day of the week (%A) and then prints the date as a string:

import datetime

date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day is/was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))
"""

from project import Project
import datetime

FILENAME = "projects.txt"
MENU = """Menu:
L - Load projects
S - Save projects
D - Display projects
F - Filter projects by date
A - Add new project
U - Update project
Q - Quit
"""


def main():
    """Manage a list of projects."""
    projects = load_file_contents(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(MENU)
    choice = input(">>> ").upper().strip()

    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load projects from: ")
            projects = load_file_contents(filename)

        elif choice == "S":
            filename = input("Enter filename to save projects to: ")
            write_to_file(filename, projects)

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            date_string = input(
                "Show projects that start after date (d/m/yyyy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)

        elif choice == "A":
            new_project = get_user_input()
            projects.append(new_project)

        elif choice == "U":
            update_project(projects)

        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(">>> ").upper().strip()


def load_file_contents(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        next(in_file)  # Skip header line
        for line in in_file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(
                parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            percent_complete = int(parts[4])
            project = Project(name, start_date, priority,
                              cost_estimate, percent_complete)
            projects.append(project)

    return projects


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    print("Incomplete projects:")
    
    print("Completed projects:")
    


def filter_projects_by_date(projects, date):
    """Display projects that start after a given date, sorted by date."""
    


def get_user_input():
    """Get user input for a new project and return a Project object."""
    name = input("Project name: ")
    date_string = input("Start date (d/m/yyyy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percent_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percent_complete)


def update_project(projects):
    """Update a project's percent complete and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project number to update: "))
    project = projects[index]

    new_percent = input("New percent complete (leave blank to keep current): ")
    if new_percent:
        project.percent_complete = int(new_percent)

    new_priority = input("New priority (leave blank to keep current): ")
    if new_priority:
        project.priority = int(new_priority)


def write_to_file(filename, projects):
    """Write the list of projects to a file."""
    with open(filename, 'w') as out_file:
        out_file.write(
            "Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n")


if __name__ == "__main__":
    main()

   """display menu
    get choice
    while choice != <quit option>
        if choice == <first option>
            <do first task>
        else if choice == <second option>
            <do second task>
        ...
        else if choice == <n-th option>
            <do n-th task>
        else
            display invalid input error message
        display menu
        get choice
    <do final thing, if needed>"""