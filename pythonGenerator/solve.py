
# Generators in Python are functions that produce values on-the-fly,
# allowing memory-efficient iteration over potentially large sequences.
# uses values without storing it into memory

## normal function
a = 0
def simple_gen():
    global a
    a = a+1
    return a
## generator returns an iterator
def simple_generator():
    yield 1 # the iterator first pointing to this
    yield 2
    yield 3
print("Normal Function Output")
print(simple_gen())
print(simple_gen())
print(simple_gen())
# Create a generator object
print("Generator Function Output")
## gen is an iterator return by the generator
gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
## genetors output with for loop
# Create a generator object
gen = simple_generator()
# or using loops you can
for v in gen:
    print(v,end=" ")
print()
## generating fibonacci series using generator
def fibo() :
    a, b=0, 1
    while True :
        yield a
        a, b = b, a + b
for fib in fibo() :
    if fib >13 : 
        break
    print(fib,end=" ")
print()

## genetor allows not to call a function directly is simply returns a iterator 
## 