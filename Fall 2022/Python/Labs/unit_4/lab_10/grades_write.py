# Program:      grades_write.py
# Programmer:   Kellen Land
# Date:         11/29/2022
# Description:  Lab #10
##############################

filename = 'grades.txt'

with open(filename, mode = 'w') as grades:
    grades.write('111 Olivera 90\n')