# Program:  hello_world.py
# Programmer:   Kellen Land
# Date: 8/31/2022
# Description:  lab 1

# initialize string variable to hold “hello, world!”
program = f"hello, world!"

# print the variable five times cascading vertically to right – use title case
print(program.title())
print(f"\t{program.title()}")
print(f"\t\t{program.title()}")
print(f"\t\t\t{program.title()}")
print(f"\t\t\t\t{program.title()}")

# print blank line
print()

# initialize string variable to hold name of person who created program
computer_scientist = "brian kernighan"

# initialize numeric variable to hold year program was created
year_created = 1978

# Use formatted string to print sentence giving credit to that person
print(f'{computer_scientist.title()} wrote the first "{program.title()}" program in {year_created}')

# print blank line 
print()
# print the variable five times cascading vertically to left – use title case
print(f"\t\t\t\t{program.title()}")
print(f"\t\t\t{program.title()}")
print(f"\t\t{program.title()}")
print(f"\t{program.title()}")
print(program.title())
print()