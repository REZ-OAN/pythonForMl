for element in [1,2,43,4]:
    print(element)
## upper shows a iteration process
# python has a built in function called __iter()___
# this method gives us the address of the segment
# then we can iterate by using next(iterator)
a = ['hey','you','should','learn','new things'] 
itr = iter(a)
print(next(itr),end=" ")   
print(next(itr),end=" ")   
print(next(itr),end=" ")   
print(next(itr),end=" ")   
print(next(itr))   

## in reversed order
itr = reversed(a)
print(next(itr),end=" ")   
print(next(itr),end=" ")   
print(next(itr),end=" ")   
print(next(itr),end=" ")   
print(next(itr))   