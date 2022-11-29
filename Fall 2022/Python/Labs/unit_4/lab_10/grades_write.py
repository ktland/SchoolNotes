# Program:      grades_write.py
# Programmer:   Kellen Land
# Date:         11/29/2022
# Description:  Lab #10
##############################

filename = 'grades.txt'

with open(filename, mode = 'w') as grades:
    grades.write('111 Olivera 90\n')
    grades.write('222 Benavides 80\n')
    grades.write('333 Gonzales 70\n')
    grades.write('444 Casas 60\n')
    grades.write('555 Ramirez 50\n')
