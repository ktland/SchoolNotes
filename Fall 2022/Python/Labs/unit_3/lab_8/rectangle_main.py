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
    
    print(f"\nThe area is {area:.0f}")
    print(f"\nThe parimeter is {perimeter:.0f}")
    
    again = input("\nWould you like to do another calculation? (y/n) ")
    if again == 'n':
        repeat = False
        
print("\nThanks for using this program. Goodbye.\n")