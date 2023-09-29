class Vehicle: 
    def __init__(self,make,model):
        self.make = make
        self.model = model
    def move(self):
        print('move')

class Truck(Vehicle):
    def move(self):
        print("truck is moving")

myCar = Vehicle('Tesla','Model 3')

print(myCar.make)

myTruck = Truck('idk','fajny')

myTruck.move()

# OOP

