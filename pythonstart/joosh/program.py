

f = open("import.txt","r")
contents = f.read()
f.close()
d = len(contents.split("\n"))

first = contents.split("\n")


for x in range(1, int(d)+1):
    lessonfilename = str(x) + "lesson"
    file = open(lessonfilename,'w')
    file.write(first[x-1])
    file.close()
    for i in range(1, int(d)+1):
        trainfilename = str(x) + "train"
        if(i!=x):
        	file = open(trainfilename,'a')
        	file.write(first[i-1])
        	file.write('\n')
        	file.close()
