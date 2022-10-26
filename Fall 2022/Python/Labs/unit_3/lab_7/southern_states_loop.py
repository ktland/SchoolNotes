# Program:      southern_states_loop.py
# Programmer:   Kellen Land
# Date:         10/26/22
# Description:  Lab 7
# ################################

# initialize a list with names of the southern states all lowercase
southern_states = ['virginia', 'tennessee', 'arkansas', 'louisiana', 'north carolina','south carolina', 'mississippi', 'alabama', 'georgia', 'florida', 'texas']

# print name of report
print("Report - Southern United States\n")

# show unsorted list using for in loop - show title case
print("UNSORTED:\n")
for state in southern_states:
    print(state.title())

# use neg index to access last element in list and show it in title case
print(f"Last state on this unsorted list: {southern_states[-1].title()}\n")

# sort the list using the sort() method and show list again in title case
southern_states.sort()
print("SORTED: \n")
print(f"{southern_states[0].title()}")
print(f"{southern_states[1].title()}")
print(f"{southern_states[2].title()}")
print(f"{southern_states[3].title()}")
print(f"{southern_states[4].title()}")
print(f"{southern_states[5].title()}")
print(f"{southern_states[6].title()}")
print(f"{southern_states[7].title()}")
print(f"{southern_states[8].title()}")
print(f"{southern_states[9].title()}")
print(f"{southern_states[10].title()}\n")

# show list again using while loop
print("SORTED: \n")
current_state = 0
while current_state < len(southern_states):
    print(f"{southern_states[current_state].title()}")
    current_state = current_state + 1
print()

# use neg index to access last element in list and show it in title case
print(f"Last state in this ordered list: {southern_states[-1].title()}\n")


# use len() function to show length of list (number of states)
print(f"\nNumber of Southern States: {len(southern_states)}\n")

# print credit line showing source of data
print("Source: simple.wikipedia.org/wiki/Southern_United_States\n")