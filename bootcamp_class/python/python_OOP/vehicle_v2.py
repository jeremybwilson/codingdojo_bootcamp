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

class Bike(Vehicle):
  def vehicle_type(self):
    return "Bike"
class Car(Vehicle):
  def set_wheels(self):
    self.wheels = 4
    return self
class Airplane(Vehicle):
  def fly(self, miles):
    self.mileage += miles
    return self

vehicle1 = Vehicle(4,8,"dodge","minivan")
print "Vehicle make is:", vehicle1.make

b = Bike(2,1,"Schwinn","Paramount")
print "Vehicle type is:", b.vehicle_type()

c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print "Vehicle has", c.wheels, "wheels"

a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage