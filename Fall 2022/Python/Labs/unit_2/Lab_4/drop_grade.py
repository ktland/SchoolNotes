# Program:      drop_grade.py
# Programmer:   Kellen Land
# Date:         10/1/2022
# Description:  Lab #4
#############################

# print report name – DROP LOWEST GRADE PROGRAM
print("DROP LOWEST GRADE PROGRAM:\n")

# create list of 5 grades and initialize
grades = [100, 80, 70, 60, 90]

# show original grades using for in Loop
print("\nGrades: ")
for grade in grades:
    print(grade)

# use sum function on grades to calculate the total
total = sum(grades)

# calculate the average by dividing total by len(grades)
average = total / len(grades)

# print number of grades using len function
print(f'Number of grades: {len(grades)}')

# print average formatted to 2 decimal places
print(f'Average: {average:.2f}')

# find the lowest grade using min function and print lowest grade
lowest_grade = min(grades)
print(f'Lowest grade: {lowest_grade}')

# get the index of the lowest grade
grade_lowest_index = grades.index(lowest_grade)

# use del statement to delete the lowest grade by passing index
del grades[grade_lowest_index]

# print LOWEST GRADE DROPPED.
print('\nLOWEST GRADE DROPPED.')

# show grades after dropping lowest grade using for in Loop
print("\nGrades: ")
for grade in grades:
    print(grade)
total = sum(grades)
average = total / len(grades)
print(f'Number of grades: {len(grades)}')
print(f'Average: {average:.2f}')
lowest_grade = min(grades)
print(f'Lowest grade: {lowest_grade}')
print()