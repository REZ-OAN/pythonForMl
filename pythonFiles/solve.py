
## creating a file
"""
   open(completepath,mode)
   mode - r reading mode
        - w write mode (creates file when doesn't exist)
        - a append mode
        - w+ read and write operation mode( creates file when doesn't exist)
        - r+ read and write operation mode
"""
file = open("./pythonFiles/fileOne.txt","w")
## writing on the file
file.write("Great You Have learned Python files")
# closing file after complete usage
file.close()

## to write after existing file
file = open("./pythonFiles/fileOne.txt","a")
file.write("\nHey Learned Appending on file")
file.close()

## reading file line by line
file = open("./pythonFiles/fileTwo.txt","r")

## reading the whole file
file_content = file.read();
file.close()
## extracting information to file
file = open("./pythonFiles/fileThree.txt","w")

for line in file_content.split('\n') :
    words = line.split()
    print(line,"wordcount : ",len(words))
    ## writing lines on file
    file.write(line+" wordCounts : "+str(len(words))+"\n")
file.close()

## if you use with then you don't have to close the file 

with open("./pythonFiles/fileThree.txt","r") as file :
    for line in file :
        print("wordCounts : ",len(line.split())," '",line,"'\n")
## to check if the file is still open or not
## true -> closed
## false -> open

print(file.closed)