## declaration of set
# creating empty set
c = set()

a = {'a','b','c','d'}
b = {'c','d','e','f','g'}

print(type(a))
print(type(b))
print(type(c))
## but can't create like this
d = {}
print(type(d))
a.add(3)
a.add(4)
a.add(23)
print(*a)
a.remove(23)
print(*a)

## set operations
print(a|b) #union
print(a&b) #intersection
print(a-b) #set difference
a = {1,2,3}
b= {2,3}
print(b<a) # subset b is a subset of a is true or false
print(a<b) # true or false

## frozen set (constant set can't add  or remove elements)
#  frozenset() is an immutable set in Python,
#  which means you cannot modify it once it's created
d = frozenset([1,4,23,2,3])
print(*d)
## but can do set operations
a = frozenset([1,2,3])
b= frozenset([1,2])
print(a|b) #union
print(a&b) #intersection
print(a-b) #set difference
print(b<a) # subset b is a subset of a is true or false
print(a<b) # true or false