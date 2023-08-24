john_expense_list = [2100,40302,393]
joe_expense_list = [102,2032,10203]

def total_expense(arr):
    total = 0
    for x in arr :
        total+=x
    return total

john_total = total_expense(john_expense_list)
joe_total = total_expense(joe_expense_list)

print("{0} total_expense : {1} \n{2} total_expense : {3}".format("jhon's",john_total,"joe's",joe_total))

## global variables with function
total = 0

# default argumented function
def sumTwo(a,b=10):
    print("a : ",a,"b : ",b)
    total = a+b
    print('Inside function : ',total)
    return total

## using default argumented function
print(sumTwo(4))

# default value will not work when arguments are passed
## positional arguments
print(sumTwo(4,6))

## Named arguments
print(sumTwo(b=10,a=3))

print('Outside Function : ',total)


