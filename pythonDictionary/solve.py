## dictionary in python
'''
It's one kind of hashing datastructure
works like map
 key ,value
'''
d={1 : 'geeks', 2: 'Abir',3 : 'for',4 : 'Ahmed',5 : 'Geeks'}
for i in range(1,6) :
     if i%2==1 :
        print(d[i],end=" ")
print()
for  i in range(1,6) :
    if i%2==0 :
        print(d[i],end=" ")
print()
## we can create nested dictionary
d={'A' : 'Apple','B' : 'Blue Berry','C' :{1 : 'Mango',2 : 'Orange',3 : 'Malta'}}
print(d['C'][2])
print(d['B'])

d=dict([(1,'geeks'),(2, 'for')])
for i in range(1,3) :
    print(d[i],end=" ")
print()
print(d.get(2))

d=dict([(1,['geeks','for','geeks']),(2,['Rezoan','Ahmed','Abir'])])
## .key() returns the keys of the dictionary in a list
print(d.keys())
## .pop(key) remove the specified key
## .popitem() remove the last key-value pair
print(d)
d.pop(1)
print(d)
d[1]=['geeks','for','geeks']
d[3]=['hello','world','yo yo']
print(d)
d.popitem()
print(d)
## values() returns all the values of the keys present in the dictionary
print(d.values())
## iterating through python dictionary
# Creating a dictionary of a person's information
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}
# Accessing values using keys
print(person["first_name"])  # Output: John
print(person["age"])         # Output: 30

# Modifying a value
person["age"] = 31
print(person["age"])  # Output: 31
# Adding a new key-value pair
person["occupation"] = "Software Engineer"
print(person)
# Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 31, 'city': 'New York', 'occupation': 'Software Engineer'}

# Removing a key-value pair
del person["city"]
print(person)
# Output: {'first_name': 'John', 'last_name': 'Doe', 'age': 31, 'occupation': 'Software Engineer'}
# Dictionary methods
keys = person.keys()
values = person.values()
items = person.items()

print(keys)    # Output: dict_keys(['first_name', 'last_name', 'age', 'occupation'])
print(values)  # Output: dict_values(['John', 'Doe', 31, 'Software Engineer'])
print(items)   # Output: dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 31), ('occupation', 'Software Engineer')])

# Iterating through keys and values
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# first_name: John
# last_name: Doe
# age: 31
# occupation: Software Engineer

for value in person.values():
    print(value)