# Program:      grades_read.py
# Programmer:   Kellen Land
# Date:         11/29/2022
# Description:  Lab #10
##############################

filename = 'gradesX.txt'

count_grades = 0
sum_grades = 0

try:
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

except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

except:
    print("An error has occurred. Please see admin.")
else:
    print(f"Number of Grades: {count_grades}")
    print(f"Average: {sum_grades/count_grades:.2f}")