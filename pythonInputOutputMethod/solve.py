## input
## in python it converts the input value into a string
name=input("Enter Your Name : ")
print("The nerd is ",name)
# the typeof type is type class
print('The type of "name" is',type(name))
## when you need integer or float
x=int(input())
y=float(input())
print(x+y,"Here x is a ",type(x)," and ","y is a ",type(y))

## taking multiple input


## we use input().split(separator,maxsplit)
x,y=input("Enter Two Numbers : ").split()
print("X : ",x,"\nY : ",y)
x,y,z=input("Enter Three Numbers : ").split()
print("X : ",x,"\nY : ",y,"\nZ : ",z)

## 2nd method
x,y=[int(x) for x in input().split()]
print("X : ",x,"\nY : ",y)
x,y,z=[int(i) for i in input().split()]
print("X : ",x,"\nY : ",y,"\nZ : ",z)



## when you want to input an array
x=list(map(int,input().split()))
print(x)
## 2nd method
x=[int(i) for i in input().split()]
print(x)

## example with separator and maxsplit
## formatted input 
## separator =mane kon char dekhe separate korbe input gulo
## maxsplit first koyta input ke split kore varibale e rakhbe baki ja thakbe ta ekta variable er moddhe jabe

x=[int(x) for x in input().split("^",2)]
print(x)

x,y,z=input().split(',',2)
print(x)
print(y)
print(z)

## formatted output
a=20
b=11
c=1999
print(a,b,c,sep="-",end=" **")
print("My Birthday ")

print("Abir loves",end=" ")
print("Roses")
## for single line output
x=[1,3,5,7,9]
print(*x)
