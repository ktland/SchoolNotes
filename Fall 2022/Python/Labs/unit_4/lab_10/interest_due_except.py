# Program:      interest_due_except.py
# Programmer:   Kellen Land
# Date:         11/29/2022
# Description:  Lab 10
######################################

# print the name of the program
print("Program - Calculate Interest on Loan:")

# set repeat flag to True
repeat = True

# while repeat
while repeat:
    amount = input("\nHow many dollars do you wish to borrow? ")
    amount = float(amount)
    interest_rate = float(input("What is the interest rate? "))
    years = int(input("How many years would you take the loan? "))
    
    total_interest = amount *  (interest_rate/100) * years
    
    output = f"\nIf you borrow ${amount:,.2f} at an interest rate of {interest_rate}%"
    output += f"\nfor {years} years, you will pay ${total_interest:,.2f} in interest"
    
    print(output)
    
    again = input("\nWould you like to run another calculation? (y/n)")
    if again == 'n':
        repeat = False
        
print("\nThanks for using this program. Goodbye!")

try:
    amount = input("\nHow many dollars do you wish to borrow? ")
    interest_rate = float(input("What is the interest rate? "))
    years = int(input("How many years would you take the loan? "))
except ValueError:
    print("Input Error >>> Please enter numbers only. You will have to start again.")
except:
    print("An error has occurred.")
else:
    total_interest = amount *  (interest_rate/100) * years
    output = f"\nIf you borrow ${amount:,.2f} at an interest rate of {interest_rate}%"
    output += f"\nfor {years} years, you will pay ${total_interest:,.2f} in interest"
    print(output)