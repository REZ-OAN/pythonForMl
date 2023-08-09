# to import array
import array as arr

"""
    arr.array(data_type,[elements])
    data_types
    int -> 'i'
    double -> 'd'
    float -> 'f'
"""
a = arr.array('f',[2.3,2.1,3.2,5.32,4.23,5.42])

for i in a:
    print(i,end=" ")
print()

## insert element

# insert front
a.insert(0,20)
print(a)
# insert back -1 indexing does not work here
a.insert(len(a),201)
print(a)
# insert anywhere
a.insert(2,10)
print(a)

## accessing elements
a[2] = 121
print(a)

## removing element from array

# removing the last element
a.pop()
print(a)

# removing any element given the index no
a.pop(1)
print(a)

## slicing an array

# -3 to last all
print(list(a[-3:]))

# 3 to 6 (6 exclusive)
print(list(a[3:6]))

# first to 4 (4 exclusive)
print(list(a[:4]))

## searching in array

# gives the first occurence index
print(a.index(121))

# if not present then through a exception
print(a.index(1))
