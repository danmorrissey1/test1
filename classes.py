class MyCar:
    wheels = 4

    def my_car_details(self):
        print("Hello, I'm your new car")


my_car = MyCar()
my_car.my_car_details()
print(my_car.wheels)


class MyCar:
    wheels = 4

    def my_car_details(self):
        print("Hello, I'm your new car")


my_car = MyCar()
my_car.my_car_details()
print(my_car.wheels)


class MyFirstCar(MyCar):
    def __init__(self):
        self.brand = "VW"

    def my_car_details(self):
        print(f'Hello, {self.brand} i have {self.wheels}')


vw = MyFirstCar()
vw.my_car_details()


class Vehicle:
    def __init__(self, brand, doors, wheels):
        self.brand = brand
        self.doors = doors
        self.wheels = wheels

    def car_greeting(self):
        print(f'Hello, {self.brand}')


veh1 = Vehicle("VW", 2, 4)
print(veh1.wheels)

veh1.car_greeting()
