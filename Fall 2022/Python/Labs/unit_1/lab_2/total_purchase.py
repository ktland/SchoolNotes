# Program:      total_purchase.py
# Programmer:   Kellen Land
# Date:         09/07/2022
# Description:  Lab 2
# ###############################

# declare constant for sales tax rate and set to 6%
TAX_RATE = 0.06

# initialize numeric variables to hold price of four sales items
price_pants = 175
price_shirt = 125
price_shoes = 300
price_belt = 100

# calc subtotal
sub_total = price_pants + price_shirt + price_shoes + price_belt

# calc sales tax
sales_tax = sub_total * TAX_RATE

# calc grand total
grand_total = sub_total + sales_tax

# print program name
print("Program:  Total Purchase")
print()

# display a single dash line
print(32 * "-")

# print purchased items
print(f"Item #1 - Pants: \t$ {price_pants:,.2f}")
print(f"Item #2 - Shirt: \t$ {price_shirt:,.2f}")
print(f"Item #3 - Shoes: \t$ {price_shoes:,.2f}")
print(f"Item #4 - Belt: \t$ {price_belt:,.2f}")

# display a single dashed line
print(32 * "-")

# Print subtotal, sales tax, and grand total
print(f"Sub Total: \t\t$ {sub_total:,.2f}")
print(f"Sales Tax: \t\t$  {sales_tax:,.2f}")
print(f"Grand Total: \t\t$ {grand_total:,.2f}")

# display double dash line
print(32 * "=")
print()