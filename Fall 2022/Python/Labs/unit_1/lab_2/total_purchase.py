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

# calc sales tax
sales_tax = subtotal * TAX_RATE

# calc grand total
grand_total = subtotal + sales_tax

# print program name
print("Program:  Total Purchase")
print()

# display a single dash line
print(32 * "-")

# print purchased items
print(f"Item #1 - Pants: \t$ {pants:,.2f}")
print(f"Item #2 - Shirt: \t$ {shirt:,.2f}")
print(f"Item #3 - Shoes: \t$ {shoes:,.2f}")
print(f"Item #4 - Belt: \t$ {belt:,.2f}")

# display a single dashed line
print(32 * "-")

# Print subtotal, sales tax, and grand total
print(f"Sub Total: \t\t$ {subtotal:,.2f}")
print(f"Sales Tax: \t\t$  {sales_tax:,.2f}")
print(f"Grand Total: \t\t$ {grand_total:,.2f}")

# display double dash line
print(32 * "=")
print()