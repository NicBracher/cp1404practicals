"""
CP1404/CP5632 - Practical 2 - Nicholas Bracher

Temperature conversion program.

EDIT 19/09/2025: Addition of functions to prac_01 temperatures.py
"""

MENU = """C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit"""


def main():
    """Take user menu selection and use the appropiate conversion function to display converted temperature."""
    choice = get_menu_selection(MENU)

    while choice != "Q":

        if choice == "C":
            celsius = get_valid_input("Enter temperature in Celsius: ")
            converted_temperature = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {converted_temperature:.1f} F")

        elif choice == "F":
            fahrenheit = get_valid_input("Enter temperature in Fahrenheit: ")
            converted_temperature = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {converted_temperature:.1f} C")

        choice = get_menu_selection(MENU)
    print("Thank you.")


def get_valid_input(prompt):
    """Get a valid input from the user."""
    temperature = float(input(prompt))

    while temperature != float(temperature):
        print("Invalid input. Please enter a number.")
        temperature = float(input(prompt))

    return temperature


def convert_celsius_to_fahrenheit(temperature):
    """Convert temperature from Celsius to Fahrenheit."""
    return temperature * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(temperature):
    """Convert temperature from Fahrenheit to Celsius."""
    return 5 / 9 * (temperature - 32)


def get_menu_selection(prompt):
    """Get a valid menu selection input from the user."""
    print(prompt)
    choice = choice = input(">>> ").upper()

    while choice != "Q" and choice != "C" and choice != "F":
        print(f"\nInvalid choice. Please choose between: \n{MENU}")
        choice = input(">>> ").upper()
    return choice


main()
