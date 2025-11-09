"""
CP1404 Practical 7 - Project Management

Time estimate: 75 minutes
Time actual: (10:25am)

"""

from project import Project
import datetime
from operator import attrgetter

FILENAME = "projects.txt"
MENU = """- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date
- (A)dd new project\n- (U)pdate project\n- (Q)uit"""


def main():
    """Menu-driven project management program with function call and class objects."""
    projects, number_of_project_loaded = load_file_contents(FILENAME)
    print(
        f"Welcome to Pythonic Project Management \nLoaded {number_of_project_loaded} projects from {FILENAME}")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            filename = input("Enter filename to load projects from: ")
            projects, number_of_project_loaded = load_file_contents(filename)
            print(
                f"Loaded {number_of_project_loaded} projects from {filename}")

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
            print("Lets add a new project")
            new_project = get_user_input()
            projects.append(new_project)

        elif choice == "U":
            update_project_details(projects)

        else:
            print("Invalid menu choice")

        print(MENU)
        choice = input(">>> ").upper()

    choice = input(f"Would you like to save to {FILENAME}? (Y/N): ").upper()
    if choice == "Y":  # Only write project updates to file if user wants to
        write_to_file(FILENAME, projects)
    else:
        print("Thank you for using custom-built project management software.")


def load_file_contents(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip header line
        for i, line in enumerate(in_file, 1):
            parts = line.strip().split('\t')  # Split by tab
            name = parts[0]
            start_date = datetime.datetime.strptime(
                parts[1], "%d/%m/%Y").date()  # datetime module converting second index string to date
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            percent_complete = int(parts[4])
            project = Project(name, start_date, priority,
                              cost_estimate, percent_complete)
            projects.append(project)

    return projects, i


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    print("Incomplete projects:")
    incomplete_projects = sorted(
        [project for project in projects if project.percent_complete < 100], key=attrgetter('priority'))
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    completed_projects = sorted(
        [project for project in projects if project.percent_complete == 100], key=attrgetter('priority'))
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects, date):
    """Display projects that start after a given date, sorted by date."""
    filtered_projects = sorted(
        [project for project in projects if project.start_date >= date], key=attrgetter('start_date'))
    for project in filtered_projects:
        print(f"  {project}")


def get_user_input():
    """Get user input for a new project and return that input as a new Project object."""
    name = input("Name: ")
    date_string = input("Start date (d/m/yyyy): ")
    start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    percentage_complete = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, percentage_complete)


def update_project_details(projects):
    """Update a project's complete percentage and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    print(projects[index])
    project = projects[index]

    new_percentage = input("New Percentage: ")
    if new_percentage != "":  # Leave percentage unchanged if blank
        project.percent_complete = int(new_percentage)

    new_priority = input("New Priority: ")
    if new_priority != "":  # Leave priority unchanged if blank
        project.priority = int(new_priority)


def write_to_file(filename, projects):
    """Write the list of projects to a file."""
    with open(filename, 'w') as out_file:
        out_file.write(
            "Name\tStart Date\tPriority\tCost Estimate\tPercent Complete\n")  # Header line, tab-delimited
        for project in projects:
            out_file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n")


if __name__ == "__main__":
    main()
