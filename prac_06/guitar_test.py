"""
CP1404/CP5632 Practical - Nicolas Bracher
Time estimate: 45 minutes
Time actual: 52 minutes

"""

from guitar import Guitar

guitar_one = Guitar("Gibson L-5 CES", 1925, 16000)
guitar_two = Guitar("Another Guitar", 2013, 500)

print(f"{guitar_one.name} get_age() - Expected 100. Got {guitar_one.get_age()}")
print(f"{guitar_two.name} get_age() - Expected 12. Got {guitar_two.get_age()}")

print(f"{guitar_one.name} is_vintage() - Expected True. Got {guitar_one.is_vintage()}")
print(f"{guitar_two.name} is_vintage() - Expected False. Got {guitar_two.is_vintage()}")
