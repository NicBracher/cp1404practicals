"""
CP1404/CP5632 - Practical 3 - Nicholas Bracher
Answer the following questions:
1. When will a ValueError occur?
    1a. When the user inputs anything other than an integer value for either the numerator or denominator.

2. When will a ZeroDivisionError occur?
    2a. When the user inputs 0 for the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    3a. yes by adding a check to make sure the denominator is not 0 before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator

    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
