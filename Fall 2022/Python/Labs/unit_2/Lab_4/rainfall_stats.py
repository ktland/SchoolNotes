# Program:      rainfall_stats.py
# Programmer:   Kellen Land
# Date:         10/1/2022
# Description:  Lab #4
#############################

# initialize string list of the months 
months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

# initialize numeric list with average monthly rainfall
inches = [1.90, 2.37, 3.06, 3.20, 5.15, 3.23, 2.12, 2.03, 2.42, 4.11, 2.57, 2.57]

# print report header – Average Monthly Rainfall 
print("Average Monthly Rainfall - 2018 - Dallas, TX\n")

# use for loop with the range function – pass len of month list 
for value in range(len(months)):
    print(f"{months[value].title()}\t\t{inches[value]:.2f}in.")

# print credit line showing source of data 
print("\nSource: www.rssweather.com\n")

# use sum function to find the total rainfall and assign to total variable 
total = sum(inches)

# dividing total by len function of list and assign to average variable 
average = total / len(inches)

# display total and average rainfall for year
print(f"Total rainfall: \t{total:.2f}")
print(f"Average rainfall: \t{average:5.2f}")
print()