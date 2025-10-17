"""
CP1404/CP5632 - Practical 5 - Nicholas Bracher
Hex colours in a dictionary
"""

COLOUR_TO_HEX = {"Absolute Zero": "#0048BA", "Acid Green": "#B0BF1A", "Black": "#000000", "Blue": "#0000FF",
                 "Cyan": "#00FFFF", "Electric Lime": "#CCFF00", "Free Speech Blue": "#3B7A57", "Candy Apple Red": "#ff0800",
                 "Magenta": "#FF00FF", "Dark Lavender": "#E6E6FA"}
colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_HEX[colour_name])
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()