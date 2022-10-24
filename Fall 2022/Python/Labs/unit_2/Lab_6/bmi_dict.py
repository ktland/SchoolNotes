# Program:      bmi_dict.py
# Programmer:   Kellen Land
# Date:         10/15/2022
# Description:  Lab 6
###########################

# define & initialize 3 parallel lists for names, heights, and weights
patient_0 = {'name': 'bob', "height": 66, "weight": 150}
patient_1 = {'name': 'betty', "height": 62, "weight": 100}
patient_2 = {'name': 'liz', "height": 50, "weight": 140}
patient_3 = {'name': 'chris', "height": 70, "weight": 110}
patients = [patient_0, patient_1, patient_2, patient_3]

# print program name and report header line
print("BMI Program:\n")
print(f"NAME \tBMI \tCLASSIFICATION")
print()

# use for in loop to traverse lists
for patient in patients:
    # calc bmi
    bmi = (patient['weight'] * 703) / (patient['height'] * patient['height'])
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
    print(f"{patient['name'].title()} \t{bmi:.2f} \t{classification}\n")