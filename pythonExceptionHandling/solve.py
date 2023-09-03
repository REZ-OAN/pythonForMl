
# x,y = [int(i) for i in input().split()]

# try :
#     z = x/y
# except Exception as e :
#     print("Exception Occured!!! ", e)
#     ## to know the name of that error
#     print("nametype : ",type(e).__name__)
#     z = None
#     print("Z : ",z)
# else :
#   print("Division Is : ", z)
 
## custom or user defined error handling

## if you want to declare your own error then 
## you have to inherit python Exception class
class Hola_Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def exception_(self):
        print("user defined exception : ",self.msg)
 
try :
    raise Hola_Accident('Car Crashed')
except Hola_Accident as e :
    e.exception_()

"""
finally 
in this block the written code executes even the upper block has some 
error in that block
"""
try :
    file = open("./pythonExceptionHandling/input.txt","r")
    print("File Status (if opened then shows False)",file.closed)
    x = 1/0
except FileExistsError as e :
    print(e)
## like in the upper block there can be thousand lines of code
## and you will not know what's raises the error
## but your file is opened and it can leak data from your code
## here finally comes
finally :
    file.close()
    print("File Status (if closed then shows True)",file.closed)
    ## it executes then program crashes :V
