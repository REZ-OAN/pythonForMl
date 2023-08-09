a = int(input())
b = float(input())
## by default it takes input as a string
c = input()
print(a,' ',type(a))
print(b,' ',type(b))
print(c,' ',type(c))

## multiple value input

# method-1 
a = [int(i) for i in input().split()]
print(a)

# method-2
b = list(map(int,input().split()))
print(b)

# input pattern
x,y,z = [float(p) for p in input().split()]
print(x," ",y," ",z)
x,y,z = list(map(str,input().split()))
print(x," ",y," ",z)
