# Program:      grades_read.py
# Programmer:   Kellen Land
# Date:         11/29/2022
# Description:  Lab #10
##############################

filename = 'grades.txt'

with open(filename, mode = 'r') as grades:
    print(f"{"ID":<10}{"Name":<10}{"Grade":>10}")
    print('==============================')
for record in grades:
    student_id, name, grade = record.split()