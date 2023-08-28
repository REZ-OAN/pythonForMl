class vehicle :
    def __init__(self,a):
        self.avg_acceleration=a
    def gerenral_uses() :
        print("General Use : Transport")
    def speed(self,s):
        v =  2*self.avg_acceleration*s
        return round(v)
class car (vehicle) :
    def __init__(self,a):
        ## super() -> refers to the parent class
        super().__init__(a)
        self.wheels=4
        self.roof = True
    def get_info(self,s):
        v = super().speed(s)
        info = {
            "type" : "Car",
            "wheels": self.wheels,
            "roof": self.roof,
            "velocity" : v
        }
        return info
    

class bike (vehicle) :
    def __init__(self,a):
        super().__init__(a)
        self.wheels=2
        self.roof = False
    def get_info(self,s):
        v = super().speed(s)
        info = {
            "type" : "Bike",
            "wheels": self.wheels,
            "roof": self.roof,
            "velocity" : v
        }
        return info
     
class MilitaryLongtruck (vehicle) :
    def __init__(self,a):
        super().__init__(a)
        self.wheels=8
        self.roof = True
    def get_info(self,s):
        v = super().speed(s)
        info = {
            "type" : "Military Long Truck",
            "wheels": self.wheels,
            "roof": self.roof,
            "velocity" : v
        }
        return info

a = car(10)
b = bike(5)
c = MilitaryLongtruck(15)

## from parent property
print(a.avg_acceleration)
print(b.avg_acceleration)
print(c.avg_acceleration)

## from parent method
print(a.speed(10))
print(b.speed(5))
print(c.speed(15))

## from individuals method
print(a.get_info(10))
print(b.get_info(5))
print(c.get_info(15))

## from individuals property
print(a.wheels)
print(b.wheels)
print(c.wheels)

""" 
for **Multiple Inheritance**
class Parent1:
    def __init__(self):
        self.value1 = 1

class Parent2:
    def __init__(self):
        self.value2 = 2

**this is important to know 
class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()  # This will invoke Parent1's __init__ method
        self.value3 = 3
    
or 

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        self.value3 = 3

child_obj = Child()
print(child_obj.value1)  # Output: 1
print(child_obj.value2)  # Output: 2
print(child_obj.value3)  # Output: 3
"""