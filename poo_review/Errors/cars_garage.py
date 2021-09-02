from typing import List


class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f"car {self.make!r} {self.model!r}"


class Garage:
    def __init__(self, **cars):
        self.cars: List = []

    def __len__(self):
        return(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried to add a {car.__class__.__name__} to \
                the garage, but you can only add 'Car' objects")
        self.cars.append(car)


ford = Garage()
fiesta = Car('Ford', 'Fiesta')
try:
    ford.add_car('Fiesta')
except TypeError:
    print("Your car was not a Car!")
