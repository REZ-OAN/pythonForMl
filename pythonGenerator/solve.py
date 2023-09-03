
# Generators in Python are functions that produce values on-the-fly,
# allowing memory-efficient iteration over potentially large sequences.
# uses values without storing it into memory

def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()
print(next(gen))
print(next(gen))
print(next(gen))
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