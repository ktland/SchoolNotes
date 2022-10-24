# Program:      state_capitals.py
# Programmer:   Kellen Land
# Date:         10/15/2022
# Description:  Lab 6
#####################################

state_capitals = {'texas': 'austin',
                        'new york': 'albany',
                        'lousiana': 'baton rouge',
                        'georgia': 'atlanta'}

print("State Capitals Listing:\n")

for state, capital in state_capitals.items():
    print(f"The capital of {state.title()} is {capital.title()}.")

print(f"\nNumber of states in this report: {len(state_capitals)}")

print("\nDeleting New York.")
del state_capitals['new york']
print(f"Number of states in this report: {len(state_capitals)}")

print("\nAdding Michigan and relisting.\n")
state_capitals['michigan'] = 'lansing'

for state, capital in state_capitals.items():
    print(f"The capital of {state.title()} is {capital.title()}.")

print(f"\nNumber of states in this report: {len(state_capitals)}")
print()