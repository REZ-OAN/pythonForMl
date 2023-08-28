
x,y = [int(i) for i in input().split()]

try :
    z = x/y
except Exception as e :
    print("Exception Occured!!! ", e)
    ## to know the name of that error
    print("nametype : ",type(e).__name__)
    z = None
    print("Z : ",z)
else :
  print("Division Is : ", z)
