# This program will print my name with an introduction and state facts about Python in a formatted output.

# declare string variable for student’s first name & initialize (lower case)
first_name = "kellen"

# declare string variable for student’s last name & initialize (lower case)
last_name = "land"

# create formatted string of student’s full name & assign to string variable
introduction_message = f"My name is {first_name.title()} {last_name.title()}."

# pass string variable to print function
print(introduction_message)

# print a blank line using print() or \n
print()

# declare string variable for python’s creator’s full name & initialize (title)
creator_first_name = "guido"
creator_middle_name = "Van"
creator_last_name = "rossum"


# print things learned about python using tab and newline escape codes:
things_learned = f"Things I have learned about Python:\n\n\t Python is a general purpose programming language.\n\t Python was created by {creator_first_name.title()} {creator_middle_name.lower()} {creator_last_name.title()} and released in 1991.\n"
print(things_learned)