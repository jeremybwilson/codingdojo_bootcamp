# instantiate class Vehicle
class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self, miles):
        self.mileage += miles
        print "You drove forward " + str(self.mileage) + " miles\n"
        return self
    def reverse(self, miles):
        self.mileage -= miles
        print "You reversed " + str(self.mileage) + " miles\n"
        return self

vehicle1 = Vehicle(4, 4, "Tesla", "Model 3")

vehicle1.drive(50).reverse(25)