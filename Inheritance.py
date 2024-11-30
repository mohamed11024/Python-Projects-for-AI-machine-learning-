class Vehicle:
    def general_usage(self):
        print("Transporting")


class Car(Vehicle):
    def __init__(self):
        print("I'm Car")
        self.wheels = 4
        self.isroof = True

    def specific_usage(self):
        print("commute to work vacation with family")    
class Motorcycle(Vehicle):
    def __init__(self):
        print("I'm Motorcycle")
        self.wheels = 2
        self.isroof = False

    def specific_usage(self):
        print("Road trip racing")    


c = Car()
c.general_usage()
c.specific_usage()

m = Motorcycle()
m.general_usage()
m.specific_usage()
