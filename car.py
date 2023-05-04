class Car:
    make = "Mercedes"
    def __init__(self, model, year, colour):
       self.model = model
       self. year = year
       self.colour = colour
    def vehicle_is(self):
        return f"This automotive is a {self.model}"
    def car_description(self):
        return f"This vehicle is {self.colour} in color."
    def year_made(self):
        return f"In the year {self.year} is when this vehicle was made."