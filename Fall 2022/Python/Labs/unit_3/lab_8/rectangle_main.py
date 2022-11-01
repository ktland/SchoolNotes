# Program:      rectangle_main.py
# Programmer:   Kellen Land
# Date:         11/01/2022
# Description:  Lab 8
#################################

import rectangle_mod

print("Program - Find Area and Perimeter of Rectangle: ")

repeat = True

while repeat:
    width = input("\nEnter the rectangle's width (inches): ")
    width = float(width)
    length = float(input("Enter rectangle's length (inches): "))
    
    area = rectangle_mod.find_area(width, length)
    perimeter = rectangle_mod.find_perimeter(width, length)
    