class Car:
    def go(self):
        print("I drive using 4 tires")


class Motorcycle:
    def go(self):
        print("I drive using 2 tires")


class Truck:
    def go(self):
        print("I drive using 8 tires")


def driving_vehicle(vehicle):
    vehicle.go()


miVehiculo = Motorcycle()

miVehiculo2 = Car()

miVehiculo3 = Truck()

# miVehiculo.go()
# miVehiculo2.go()
# miVehiculo3.go()

driving_vehicle(miVehiculo)
