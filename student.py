# class Student:
#    name = "Emily" 
#    age = 21
#    school = "AkiraChix"
# the above is how to create a class in python

# INSTANCE VARIABLES
# allow us to create objects with different ifferent attribute values
# An object has attributes and behaviours
# Behaviours is what the object can do
# Attributes are more of characteristics. they can't make the object do anything.

# Update the Student Class to include these attributes - first_name, last_name, age, country
    #  - Add these methods to the Student class
    #          - show_full_name
    #          - year_of_birth
    #          - show_initials
class Student:
    school = "AkiraChix"
    def __init__(self, age , nationality, first_name, last_name, country, birth, abbreviations):
        self.age = age
        self.nationality = nationality
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.birth = birth
        self.abbreviations = abbreviations    
    def greet_Student(self):
        return f"Hello {self.first_name} welcome to {self.school}, are you proud to be {self.nationality}."
    def show_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def year_of_birth(self):
        return f"{self.birth}" 
    def show_initials(self):
        return f"{self.abbreviations} {self.abbreviations}"      

