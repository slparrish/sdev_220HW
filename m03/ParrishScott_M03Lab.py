# ParrishScott_M03Lab.py
# By: Scott Parrish
# 11/13/23
# v: 0.1
# A simple program to implement a vehicle class and automobile subclass.

class Vehicle():
    def __init__(self, _type) -> None:
        self.type = _type
    

class Automobile(Vehicle):
    def __init__(self, _type, year, make, model, doors, roof) -> None:
        super().__init__(_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Return a nice formatted string when printing the object
    def __str__(self):
        return f'Vehicle type: {self.type}\nYear: {self.year}\nMake: {self.make}\
              \nModel: {self.model}\nDoors: {self.doors}\nRoof: {self.roof}'



def make_Auto():
    """Prompt the user to enter information to populate the Automobile object attributes"""
    _type = 'car'
    print(f'Lets get some details about the {_type}.')
    year = str(input(f'What year is the {_type}? '))
    make = input('Who is the manufacturer? ')
    model = input('What model is it? ')
    doors = str(input('How many doors does it have? '))
    roof = input(f'Does the {_type} have a sunroof or solid roof? ')
    return Automobile(_type, year, make, model, doors, roof)


def main():
    my_car = make_Auto()
    print(my_car)
    # my_other_car = Automobile('car', 1972, 'Chevrolet', 'Corvette', 2, 'Sun Roof')
    # print(my_other_car)

if __name__ == "__main__":
    main()