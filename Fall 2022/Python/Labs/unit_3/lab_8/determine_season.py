# Program:      determine_season.py
# Programmer:   Kellen Land
# Date:         11/01/2022
# Description:  Lab 8
###################################

# function definition determine_season – receives temp and returns season
def determine_season(input_temp):
    """Receives temp and returns probable season"""
    
    season = ""
    
    if input_temp > 130 or input_temp < -20:
        season = "invalid"
    elif input_temp >= 90:
        season = "summer"
    elif input_temp >= 70 and input_temp < 90:
        season = "spring"
    elif input_temp >= 50 and input_temp < 70:
        season = "fall"
    elif input_temp < 50:
        season = "winter"
    else:
        season = ""
    
    return season

# print name of program
print("Program - Determine Season: \n")

# set repeat flag to True
repeat = True

while repeat:
    input_temp = input("\nEnter the temperature (in Fahrenheit): ")
    input_temp = float(input_temp)
    
    season = determine_season(input_temp)
    
    print(f"Based on the temperature of {input_temp}, it is most likely {season.title()}.")
    
    again = input("\nWould you like to enter another temperature? (y/n) ")
    if again =='n':
        repeat = False

print("\nThanks for using this program. Goodbye!\n")