"""
CP1404/CP5632 - Practical 3 - Nicholas Bracher
"""

# What did you see on line 1?
# A single integer number everytime it was run

# What was the smallest number you could have seen, what was the largest?
# 5 & 20

# What did you see on line 2?
# A single integer number that was between 3 and 9 inclusiive and an odd number

# What was the smallest number you could have seen, what was the largest?
# 3 & 9

# Could line 2 have produced a 4?
# No because it was set to start at 3 and was in steps of 2 so it would only produce odd numbers

# What did you see on line 3?
# A single floating point number with random numbers within 2.5 and 5.5 inclusive

# What was the smallest number you could have seen, what was the largest?
# 2.5 & 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.

import random
print(random.randint(1, 100))
