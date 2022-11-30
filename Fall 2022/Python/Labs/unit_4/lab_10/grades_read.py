# Program:      grades_read.py
# Programmer:   Kellen Land
# Date:         11/29/2022
# Description:  Lab #10
##############################

filename = 'grades.txt'

count_grades = 0
sum_grades = 0

with open(filename, mode = 'r') as grades:
    print(f'{"ID":<10}{"Name":<10}{"Grade":>10}')
    print('==============================')
    for record in grades:
        student_id, name, grade = record.split()
        grade = int(grade)
        print(f"{student_id:<10}{name:<10}{grade:>10}")
        count_grades = count_grades + 1
        sum_grades = sum_grades + grade
    print('=' * 30)

print(f"Number of Grades: {count_grades}")
print(f"Average: {sum_grades/count_grades:.2f}")

try:


except FileNotFoundError:

except:

else:
    