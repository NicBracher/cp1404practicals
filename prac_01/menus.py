""" 
CP1404/CP5632 - Practical - Nicholas Bracher
Simple menu program

Pseudocode:

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""

MENU = """(H)ello \n(G)oodbye \n(Q)uit"""

name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":

    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid option")

    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")