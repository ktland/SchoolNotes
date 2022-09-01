# This program will print my name with an introduction and state facts about Python in a formatted output.

# Define variables for person's name
first_name = "kellen"
last_name = "land"

# Introduce yourself
introduction_message = f"My name is {first_name.title()} {last_name.title()}\n"
print(introduction_message)

# Define variable for Python creator's name
creator_first_name = "guido"
creator_middle_name = "Van"
creator_last_name = "rossum"


# List facts that I've learned about Python using Python creator's variables
things_learned = f"Things I have learned about Python:\n\n\t Python is a general purpose programming language.\n\t Python was created by {creator_first_name.title()} {creator_middle_name.lower()} {creator_last_name.title()} and released in 1991.\n"
print(things_learned)