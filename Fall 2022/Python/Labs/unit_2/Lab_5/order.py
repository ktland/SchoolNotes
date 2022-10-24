# Program:      order.py
# Programmer:   Kellen Land
# Date:         10/8/2022
# Description:  Lab 5
###########################

# define list of menu items
menu_items = ["hamburger", "soda", "fries", "chicken nuggets", "coffee", "cheeseburger"]

# define list of prices that correspond to menu items
menu_prices = [3.00, 1.25, 2.00, 2.90, .90, 3.40]

# define list containing a customer order
customer_order = ["hamburger", "fries", "soda", "pizza"]

# inintialize total_price to 0.0
total_price = 0.0

# print report header – Order Detail
print("Order Detail:\n")

# use for in loop to traverse customer order
for order in customer_order:
    if order in menu_items:
        print(f"Adding {order.title()}.")
        order_index = menu_items.index(order)
        print(f"Price: ${menu_prices[order_index]:.2f}\n")
        total_price = total_price + menu_prices[order_index]
    else:
        print(f"Sorry, we don't have {order}.\n")

# print order is ready
print("Your order is ready!")

# print total price
print(f"Total Price: ${total_price:.2f}")
print()