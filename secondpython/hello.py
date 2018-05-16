# file = open('we.txt','w')

# file.write('Hello World') 
# file.write('\n') 

# file.write('1') 
# file.write('2') 
# file.write('3') 

# file.close()

# file = open('we.txt','r') 

# f = file.read()

# print f

# file.close()

f = open("we.txt","r")
contents = f.read()
f.close()
d = len(contents.split("\n"))

# for row in contents.split("\n"):
# 	file = open(row,'w')
# 	file.write(row) 
# 	file.write('\n') 
# 	# file.write(str(d)) 
# 	file.close()

first = contents.split("\n")


for x in range(0, int(d)):
    if(x==0):
    	file = open('1lesson','w')
    	file.write(first[0])
    	file.close()
    else :  
    	file = open('1train','a')
    	file.write(first[x])
    	file.write('\n')
    	file.close()
    	


