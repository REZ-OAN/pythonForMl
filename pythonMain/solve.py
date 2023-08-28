## does python have any entry point 
## by default there is no entry point in python
## but here is a way to have it 
## using __name__ == __main__
"""
  to run python file in terminal
  goto the directory where the file is 
  then 
  in linux 
  python3 file_name.py
  in windows
  python file_name.py

"""
def cube_(a) :
    print("__name__" , __name__)
    return a*a*a

## when name is change
if __name__ == "__main__" :
  
    print("I'm in solve.py ")
    print(cube_(3))

