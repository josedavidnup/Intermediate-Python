class Car:
    length = 20
    width = 120
    tires = 4
    on = False

    def go(self):
        self.on = True

    def stop(self):
        self.on = False

    def status(self):
        if self.on:
            return "The car is going"


my_car = Car()

print(my_car.length)
print(my_car.tires)
my_car.go()
print(my_car.status())
