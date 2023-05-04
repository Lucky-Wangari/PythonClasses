# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.

# Discuss in your group and come up with the attributes and three methods (behaviours) for each class and implement them

# Then do the following in the interpreter 
# Create two instances of each class. 
# Call each of the methods you defined.
# Once you verify all the methods are working, commit your work, push to GitHub and submit.

class Fruit:
    eaten = "Fresh"
    def __init__(self, taste, type, name):
        self.taste = taste
        self.type = type
        self. name = name
    def description_of(self):
        return f"Majority of fruits are {self.taste}."
    def feeling_while(self):
        return f"Biting into a {self.type} fruit on a sunny day is refreshing."
    def availability_of_some(self):
        return f"{self.name} fruits are not avaialable throughout the year."
    

    