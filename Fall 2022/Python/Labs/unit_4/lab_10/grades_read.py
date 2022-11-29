# Program:      grades_read.py
# Programmer:   Kellen Land
# Date:         11/29/2022
# Description:  Lab #10
##############################

filename = 'demo_file.txt'

f = open(filename, mode = 'w')
f.write("Woops. I have deleted the contents!\n")
f.close()