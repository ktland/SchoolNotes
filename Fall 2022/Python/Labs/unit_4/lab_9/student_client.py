# Program:      student_client.py
# Programmer:   Kellen Land
# Date:         11/18/2022
# Description:  Lab #9
#################################

from student_class import Student

s1 = Student("bob benavides", 65)
s2 = Student("melissa gonzales", 17)

print("Report - Student Information:")

s1.describe_student()
s2.describe_student()

s1.set_age(-10)
s2.set_age(13)

s2.name = "melissa cantu"
#s2.set_name("")
#s2.set_name("melissa cantu")

s1.describe_student()
s2.describe_student()

print()