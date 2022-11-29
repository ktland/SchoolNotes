# Program:      student_class.py
# Programmer:   Kellen Land
# Date:         11/18/2022
# Description:  Lab #9
################################

"""Student class definition"""

class Student:
    """Student class to model a student"""

    def __init__(self, new_name, new_age):
        """Initialize a Student object"""
        self.name = new_name.title()
        self.age = new_age

    def set_age(self, new_age):
        """Validate - allow update of age if > 0. Provide feedback either way."""
        if new_age > 0:
            self.age = new_age
            print(f"\n*** Attempt to change {self.name}'s age to {new_age}.")
            print(f"\n>>> Age was updated for {self.name}.")
        else:
            print(f"\n*** Attempt to change {self.name}'s age to {new_age}.")
            print(f">>> Age for {self.name} cannot be <= 0. NO update made.")

    def set_name(self, new_name):
        """Validate - allow update to name if update is not empty string."""
        if new_name != "":
            print(f"\n*** Attempt to change name for {self.name}. ")
            self.name = new_name.title()
            print(f">>> Name was updated to {self.name}")
        else:
            print(f"\n*** Attempt to change {self.name} to empty string.")
            print(f">>> Name for {self.name} was not changed.")

    def determine_type(self):
        """return the probable level of schooling give age."""
        if self.age >= 0 and self.age <= 4:
            type = "Preschool"
        elif self.age == 5:
            type = "Kindergarten"
        elif self.age >= 6 and self.age <= 10:
            type = "Elementary School"
        elif self.age >= 11 and self.age <= 13:
            type = "Middle School"
        elif self.age >= 14 and self.age <= 17:
            type = "High School"
        elif self.age >= 18:
            type = "College"
        else:
            type = ""

        return type

    def describe_student(self):
        """display a summary of student information"""
        print(f"\nName: \t{self.name}")
        print(f"Age: \t{self.age}")
        print(f"Type: \t{self.determine_type()}")

