import math
## declaration and definition of a class
## __init__() -> like constructor function like c++
## self -> works like this keyword like in c++

class complex_ :
    def __init__(self,real=0,img=0) :
        self.real = real
        self.img = img
    def get_comp(self) :
        print("img",self.img,"real",self.real)
        mod = round((round(self.real**2) + round(self.img**2))**.5)
        arg = math.atan(self.img/self.real)
        return {"mod":mod,"arg":(arg*180/math.pi)}
    def add_comp(self,c2):
        c = complex_(0,0)
        c.real = self.real+c2.real
        c.img = self.img+c2.img
        return c 
c1 = complex_()
c2 = complex_(4,3)
c1.real = 1
c1.img = 3**.5
c = c1.add_comp(c2)
print("Real : ",c.real,"Imaginary : ", c.img)

info = c1.get_comp()
print(info['arg'])
print(info['mod'])