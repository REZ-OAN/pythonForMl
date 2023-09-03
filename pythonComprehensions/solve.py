## list comprehensions
a = [1,22,21,21,22,12,3,232,211,221,3,2,42,53,5,32]
## listing all the even numbers in a
evens = [x for x in a if x%2==0 ]
print(*evens)
## listing all the odd numbers in a
odds = [x for x in a if x%2==1]
print(*odds)

## finding squares of those numbers in a which is divisible by 3
sq = [x*x for x in a if x%3==0]
print(*sq)

## comprehension structure [what_we_need loop_in_iterable_item condition]

## set comprehensions
s = set([1,3,4,3,2,4,23,2,4,3,5,3,5,6,6,3,8,2])
print(*s)
evens = {x for x in s if x%2==0}
print(*evens)

## dictionary comprehensions
cities = ["Dhaka","Chittagong","Rajshahi","Khulna","Sylhet"]
division = [
    "Dhaka Division",
     "Chittagong Division",
     "Rajshahi Division",
     "Khulna Division",
     "Sylhet Division"
]
division_cities = zip(division,cities) ## creates tuple
print(*division_cities)
division_cities = {div:cit for div,cit in zip(division,cities)}
print(division_cities)