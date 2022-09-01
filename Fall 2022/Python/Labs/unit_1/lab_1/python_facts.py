# Program:  python_facts.py
# Programmer:   Kellen Land
# Date: 8/31/2022
# Description:  lab 1

# declare string variable for student’s first name & initialize (lower case)
first_name = "kellen"

# declare string variable for student’s last name & initialize (lower case)
last_name = "land"

# declare string variable for python’s creator’s full name & initialize (title)
python_creator = "Guido van Rossum"

# create formatted string of student’s full name & assign to string variable
message = f"My name is {first_name.title()} {last_name.title()}."

# pass string variable to print function
print(message)

# print a blank line using print() or \n
print()

# print things learned about python using tab and newline escape codes:  
print("Things I have learned about Python:\n\t")

# print string literal saying python is general purpose
print("\tPython is a general purpose programming language.")

# use f string to show Pythons creator
print(f"\tPython was created by {python_creator} and released in 1991.\n")

# use print() to create a new line
print()