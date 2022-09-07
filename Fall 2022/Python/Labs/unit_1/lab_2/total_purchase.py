# Program:      total_purchase.py
# Programmer:   Kellen Land
# Date:         09/07/2022
# Description:  Lab 2
# ###############################

# declare constant for sales tax rate and set to 6%
TAX_RATE = 0.06

# initialize numeric variables to hold price of four sales items
pants = 175
shirt = 125
shoes = 300
belt = 100

# calc subtotal
subtotal = pants + shirt + shoes + belt
print(subtotal)
# calc sales tax
sales_tax = subtotal * tax_rate
print(sales_tax)
# calc grand total
grand_total = subtotal + sales_tax
print(grand_total)
