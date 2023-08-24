'''
  Dynamic Array like vectors in c++
  creating a list
  L=[]
  initialization
  L=[10,20,30]
  But difference is we can store different type of data in a list
  L=[120,10,'Geeks','al',1991]
  multidimentional list
  L=[[10,20,30],[10,15,20]]
  we can access data with negative indexing
'''
## taking input in list
s=input()
a=s.split(' ')
print(a)
'''
   But in this method every index contains a 
   string so we need to convert it to integer
   to use as a number
'''
##size of the list
n=int(input())
## using map we get the specific data types value
'''
  list(map(data_type,input().strip().split()))[:size]
'''
a=list(map(int,input().strip().split()))[:n]
print(a)
## using list comprehension and typecasting
a=[int(x) for x in input().split()]
## here no need to specify the size1
print(len(a))
print(a)
a=[str(x) for x in input().split()]
print(len(a))
print(a)

## .insert(pos,element)
a=[1,2,3,4]
a.insert(0,0)
a.insert(2,19)
print(a)
## .extend or .append only insert elements to the end of the list
## .extend concate two lists
## .append concate only one value
## complexity in extend method O(n)
##            in append method O(1)
##            in insert method O(n)
a.extend([10,11,12])
print(a)
## reversing a list
a.reverse()
print(a)
## .remove(val) just remove a specific value
## duplicate value thakle only one will be removed
## first occurrence ta shudu
## .remove() time complexity O(n)

a=[1,1,2,3,3,3,2,4]
a.remove(2)
print(a)
## .pop() without arg will delete the last element here complexity O(1)
## .pop() with arg will delete a value on the specific position here complexity O(n)
a.pop()
print(a)
a.pop(3)
print(a)

## 2d list input

# method-1
n=int(input())
a=[[int(x) for x in input().split()] for i in range(0,n)]
print(a)
for i in range (0,n) :
    print(len(a[i]),": ",a[i])
# method-2

## .append() to insert element to the back
n,m= [int(x) for x in input().split()]
l=[]
for i in range(0,n) :
    val=list(map(int,input().strip().split()))[:m]
    l.append(val)

print(l)

## splicing of a list

# list[a:b] a to b (exclusive)
a=[x for x in range(1,21)]
b=a[1:-2]
print(b)
c=a[-5 : -1]
print(c)


## sorting 

a=[3,2,-1,-20,35,32]
# sort in ascening order
a.sort() 
print(a)
# sort in descending order
a.sort(reverse=True) 
print(a)

## list concatenation
food = ['pasta','bread','beef curry','mutton curry']
fruit = ['apple','mango','banana']
new_food = food+fruit

## we can't do new_food + 'lichi'
new_food = new_food + ['lichi']
print(new_food)

print('apple' in new_food )
print('pasta' in fruit)
