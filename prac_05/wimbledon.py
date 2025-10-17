"""
CP1404/CP5632 - Practical 5 - Nicholas Bracher

Wimbledon
Estimate: 30 minutes
Actual: 

Write a program to read this file, process the data and display processed information:

the champions and how many times they have won.
the countries of the champions in alphabetical order
Requirements and Hints
You need to store the data in appropriate data structures.
The solution uses: a list of lists, a dictionary and a set.

The file is not in simple ASCII format but UTF-8 with a byte order mark, or BOM.
You can account for this by setting the encoding like:

with open(filename, "r", encoding="utf-8-sig") as in_file:
For the final output of countries, use the join method to create a single string.

Use functions for each logical step/chunk of the program.
If you write it all in main to start with, that's fine, but then refactor it.
The solution uses 4 functions including main.

Sample output (truncated)
Wimbledon Champions: 
Rod Laver 2
...
Lleyton Hewitt 1
Roger Federer 8
Rafael Nadal 2
Novak Djokovic 7
Andy Murray 2

These 12 countries have won Wimbledon: 
AUS, CRO, ESP, FRG, GBR, GER, NED, SRB, SUI, SWE, TCH, USA
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon winners from file and display processed information."""
    champions = process_file(FILENAME)
    champion_wins = count_champion_wins(champions)
    display_champion_details(champion_wins, champions)
    # display_countries(champions)


def process_file(filename):
    """Process the given file and return a list of champions."""
    champions = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            year = parts[0]
            country = parts[1]
            name = parts[2]
            champions.append([year, country, name])
    return champions


def count_champion_wins(champions):
    """Count the number of wins for each champion and return it as a dictionary."""
    names = {champion[2] for champion in champions}
    return {name: sum(1 for champion in champions if champion[2] == name) for name in names}


def display_champion_details(champion_wins, champions):
    """Display the number of wins for each champion."""
    print("Wimbledon Champions:")
    for name, wins in champion_wins.items():
        print(f"{name} {wins}")

    countries = {champion[1] for champion in champions}
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
