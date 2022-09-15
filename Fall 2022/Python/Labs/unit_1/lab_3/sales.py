# Program:      sales.py
# Programmer:   Kellen Land
# Date:         09/12/22
# Description:  Lab 3
# #########################

# initialize list of days of week starting with Monday abbreviated lowercase
days_of_week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

# initialize daily sales list corresponding to days of week
sales_list = [1000, 2000, 3000, 4000, 5000, 6000, 7000]

# print report header – Sales Report
print("ACME Stores Incorporated Sales Report: \n")
print("Current Sales: \n")

# print current sales with formatted days and sales as currency
print(f"{days_of_week[0].title()}:\t${sales_list[0]:,.2f}")
print(f"{days_of_week[1].title()}:\t${sales_list[1]:,.2f}")
print(f"{days_of_week[2].title()}:\t${sales_list[2]:,.2f}")
print(f"{days_of_week[3].title()}:\t${sales_list[3]:,.2f}")
print(f"{days_of_week[4].title()}:\t${sales_list[4]:,.2f}")
print(f"{days_of_week[5].title()}:\t${sales_list[5]:,.2f}")
print(f"{days_of_week[6].title()}:\t${sales_list[6]:,.2f}\n")

# print projected 5% increase in sales using same formatting as before
print("Projected 5% Increase:\n")
print(f"{days_of_week[0].title()}:\t${sales_list[0] * .05 + sales_list[0]:,.2f}")
print(f"{days_of_week[1].title()}:\t${sales_list[1] * .05 + sales_list[1]:,.2f}")
print(f"{days_of_week[2].title()}:\t${sales_list[2] * .05 + sales_list[2]:,.2f}")
print(f"{days_of_week[3].title()}:\t${sales_list[3] * .05 + sales_list[3]:,.2f}")
print(f"{days_of_week[4].title()}:\t${sales_list[4] * .05 + sales_list[4]:,.2f}")
print(f"{days_of_week[5].title()}:\t${sales_list[5] * .05 + sales_list[5]:,.2f}")
print(f"{days_of_week[6].title()}:\t${sales_list[6] * .05 + sales_list[6]:,.2f}\n")