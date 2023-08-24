## demonstrating module uses using math module
import math

print(math.pi)

## to know the methds and properties of math modlue
print(dir(math))

print(math.floor(3.6544))
print(math.ceil(34.3))

import calendar
cal = calendar.month(1999,11)
print(cal)

## we can goto to this link to find the module list that python
## offers https://docs.python.org/3/py-modindex.html

## importing self created modules
import myFunctions as mFn

## calling functions from created module
print(mFn.cube_(2))
print(mFn.sq_(3))

## importing modules from another folder 
import myModules.myFunctions   as mF 

print(mF.log_b(3,9))

## import modlues from a folder which is not in you directory but in computer location
"""
  import sys
  sys.path.append("copy the actual path of that folder containing modules")
  import module_name 
  then use it

 """