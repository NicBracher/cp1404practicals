"""
CP1404/CP5632 - Practical - nicholas Bracher

Pseudocode for temperature conversion:

else if choice == 'F'
fahrenheit = get input 'Fahrenheit: '
celsius = 5 / 9 * (fahrenheit - 32)
display 'Result: (celsius)'
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit \nF - Convert Fahrenheit to Celsius \nQ - Quit"""

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "C":
            celsius = get_valid_input("Enter temperature in Celsius: ")
            fahrenheit = convert_temperature(choice, celsius)
            print(f"Result: {fahrenheit:.2f} F")

        elif choice == "F":
            fahrenheit = get_valid_input("Enter temperature in Fahrenheit: ")
            fahrenheit = convert_temperature(choice, fahrenheit)
            print(f"Result: {celsius:.1f} C")

        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_input(prompt):
    """Get a valid input from the user."""
    temperature = float(input(prompt))
    while temperature != float(temperature):
        print("Invalid input. Please enter a number.")
        temperature = float(input(prompt))
    return temperature


def convert_temperature(choice, temperature):
    """Convert temperature from Celsius to Fahrenheit or vice versa."""
    if choice == "C":
        converted_temp = temperature * 9.0 / 5 + 32
    else:
        converted_temp = 5 / 9 * (temperature - 32)
    return converted_temp


main()
