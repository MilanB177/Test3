import random


class Car:
    color = "red"
    max_speed = 0  # in km/h
    velocity = 0  # in km/h
    heading = 0  # in degrees
    traveltime = 0  # in seconds

    def __init__(self):
        """When this class is instantiated, generate some interesting actual random values"""
        self.color = random.choice(["green", "yellow", "white", "blue", "red", "purple"])
        self.heading = random.randint(0, 360)
        self.max_speed = random.randint(30, 130)
        self.velocity = random.randint(0, self.max_speed)
        self.traveltime = random.randint(0, 1000)

    def traveled_distance(self):
        """calculates the distance this car traveled given the time and velocity"""
        result = self.velocity * (self.traveltime / 3600)  # in km
        return result

    def print_properties(self):
        print(self.color + " " + str(self.velocity) + "km/h " + str(
            self.heading) + "deg " + str(self.traveled_distance()) + "km")


cars = []
while cars.__len__() < 100:
    new_car = Car()
    new_car.print_properties()
    cars.append(new_car)

print(cars.__len__())
