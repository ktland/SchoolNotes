# Program:      bmi.py
# Programmer:   Kellen Land
# Date:         10/8/2022
# Description:  Lab 5
###########################

# define & initialize 3 parallel lists for names, heights, and weights
names = ["bob", "betty", "liz", "chris"]
heights = [66, 62, 50, 70]
weights = [150, 100, 140, 110]

# print program name and report header line
print("BMI Program:\n")
print(f"NAME \tBMI \tCLASSIFICATION")
print()

# use for in loop to traverse lists
for value in range(len(names)):
    # calc bmi
    bmi = (weights[value] * 703) / (heights[value] * heights[value])
    # provide feedback based on bmi
    if bmi >= 25:
        classification = "Overweight"
    elif bmi >= 18.5:
        classification = "Healthy"
    elif bmi >= 16:
        classification = "Underweight"
    else:
        classification = "Invalid"
    # detail line
    print(f"{names[value].title()} \t{bmi:.2f} \t{classification}\n")