# Program:      guess_number.py
# Programmer:   Kellen Land
# Date:         11/18/2022
# Description:  Lab #9
###############################

from random import randint

rand_num = randint(1, 10)
print(f"rand # is {rand_num}")

repeat = True
guessing = True
guess_num = input("I'm thinking of a number between 1 and 10! Try to guess the number I'm thinking of: ")
guess_num = float(guess_num)

while guessing:
    if guess_num == rand_num:
        again = input("That's it! Would you like to play again? (yes/no) ")
        if again == 'no':
            repeat = False
            guessing = False
            print("\nThanks for playing!")
        elif again == 'yes':
            print()
            # break
            guessing = False
    elif guess_num > rand_num:
        guess_num = int(input("Too high! Guess again: "))
    elif guess_num < rand_num:
        guess_num = int(input("Too low! Guess again: "))
print()