"""
CP1404/CP5632 Practical - Nicolas Bracher
Time estimate: 30 minutes
Time actual: 42 minutes
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine and return True if the programming language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Format and return a string of information."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
