# Creating an empty tuple
empty_tuple = ()

# Creating a tuple with elements
fruits = ("apple", "banana", "orange")

# Tuples can also be created without parentheses
coordinates = 1, 2
# Accessing elements using indexing
print(fruits[0])  # Output: "apple"

# Accessing elements using negative indexing
print(fruits[-1])  # Output: "orange"
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# orange
# Unpacking a tuple into variables
x, y = coordinates
print(x)  # Output: 1
print(y)  # Output: 2

# Creating a nested tuple
person = ("John", "Doe", (1990, 5, 15))
print(person[2])         # Output: (1990, 5, 15)
print(person[2][0])      # Output: 1990
#concatenation of tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
# slicing tuples
numbers = (1, 2, 3, 4, 5)
subset = numbers[1:4]
print(subset)  # Output: (2, 3, 4)
# tuple methods
numbers = (1, 2, 2, 3, 4, 2)
print(numbers.count(2))   # Output: 3 (count occurrences of 2)
print(numbers.index(3))   # Output: 3 (index of the first occurrence of 3)

## tuples are immutable 
# you can't do numbers[1]=100

