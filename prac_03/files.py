"""
CP1404/CP5632 - Practical 3 - Nicholas Bracher
"""

# 1.
print("Question 1:")
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
print("Question 2:")
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

# 3.
print("Question 3:")
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    print(f"Output: {first_number + second_number}")

# 4.
print("Question 4:")
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
    print(f"Total: {total}")
