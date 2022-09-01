# This program will print my name with an introduction and state facts about Python in a formatted output.

# declare string variable for student’s first name & initialize (lower case)
first_name = "kellen"

# declare string variable for student’s last name & initialize (lower case)
last_name = "land"

# declare string variable for python’s creator’s full name & initialize (title)
creator_first_name = "guido"
creator_middle_name = "Van"
creator_last_name = "rossum"

# create formatted string of student’s full name & assign to string variable
introduction_message = f"My name is {first_name.title()} {last_name.title()}."

# pass string variable to print function
print(introduction_message)

# print a blank line using print() or \n
print()

# print things learned about python using tab and newline escape codes:
things_learned = "Things I have learned about Python:\n\t"  
print(things_learned)

# print string literal saying python is general purpose
general_purpose = "\tPython is a general purpose programming language."
print(general_purpose)

# use f string to show Pythons creator
python_creator = f"\tPython was created by {creator_first_name.title()} {creator_middle_name.lower()} {creator_last_name.title()} and released in 1991.\n"
print(python_creator)