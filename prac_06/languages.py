"""
CP1404/CP5632 Practical - Nicholas Bracher

Time estimate: 30 minutes
Time actual: 42 minutes

"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]

# Hand written code:
print("The dynamically typed languages are:")
for language in programming_languages:
    is_dynamic = language.is_dynamic()
    if is_dynamic:
        print(language.name)
