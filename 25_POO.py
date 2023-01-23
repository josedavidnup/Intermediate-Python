class Car:
    def __init__(self):
        self.__length = 20
        self.__width = 120
        self.__tires = 4
        self.__on = False

    def go(self, going):

        self.__on = going

        if self.__on:
            checking = self.__checking_inside()

        if self.__on and checking:
            return "The car is going"
        elif self.__on and checking == False:
            return "Something went wrong"
        else:
            return "The car has stopped"

    def stop(self):
        self.__on = False

    def status(self):
        print(
            f"The car has {self.__tires} tires. {self.__length} of length and {self.__width} of width."
        )

    def __checking_inside(self):
        print("Checking engine")

        self.gas = "ok"
        self.oil = "ok"
        self.door = "closed"

        if self.gas == "ok" and self.oil == "ok" and self.door == "closed":
            return True
        else:
            return False


my_car = Car()

# print(my_car.length)
# print(my_car.__tires)
print(my_car.go(True))
print(my_car.status())

print(
    "---------------------------Here it is the second object------------------------------------"
)


my_car2 = Car()
# print(my_car2.length)
# print(my_car2.__tires)
print(my_car2.go(False))
print(my_car2.status())
