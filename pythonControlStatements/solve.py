# for loop
l=['rezoan','ahmed','abir']
for i in l :
    print(i,end=" ")
print()

for i in range(19):
    print(i,end=" ")
print()
for i in range(10,19):
    print(i)
# dictionary access with key,value pair
d=dict([('xyz',123),('abc',456)])
for key,value in d.items() :
    print(key ,' ',value)
s = "Rezoan Ahmed Abir";
for i in s :
    print(i,end="   ")
print()
# spliting the string where space is the delimeter
for i in s.split():
    print(i,end=",  ")
print()

## while loop

i = 10
while i < 110 :
    i**=2
    print(i)

i = 0 
while i<10:
    i+=1
    if i%3 == 0:
        continue
    elif i%5 == 0:
        break
    else:
        print(i)
    
