# Program:      interest.py
# Programmer:   Kellen Land
# Date:         09/06/2022
# Description:  Lab 2
# #########################

# declare and initialize variables for years, rate, and loan
years = 15
rate = 6
loan = 5000

# calculate total interest ( interest = loan * (rate/100) * years
interest = loan * (rate / 100) * years

# use formatted strings to show output
print(f"Loan amount: \t${loan}")
print(f"Interest rate: \t{rate}%")
print(f"No. of years: \t{years}")
print(f"Interest paid: \t${interest:,.2f}")
print()