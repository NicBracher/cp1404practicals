"""
CP1404/CP5632 - Practical 5 - Nicholas Bracher
World Occurrences
Estimate: 25 minutes
Actual: 27 minutes
"""

user_string_input = input("Enter a string: ").split()
word_to_count = {}

for word in user_string_input:
    word_to_count[word] = word_to_count.get(word, 0) + 1

max_length = max(len(word) for word in list(word_to_count.keys()))

for word, count in sorted(word_to_count.items()):
    print(f"{word:<{max_length}} : {count}")
