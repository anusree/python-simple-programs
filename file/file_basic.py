#Read all lines from the file and this is very fast and memory efficient
f=open('file1','r') 
for x in f:
	print x
f.close()

##################################
#This also read all lines from the file it is not memory efficient because it read all data from the file and put it into the memory
f=open('file1','r')
for x in f.readlines():
        print x
f.close()

##################################
#list(f) read all lines from the file in a list
f=open('file1','r')
print list(f)
f.close()

##################################
#write(string) writes the content of string to the file
f=open('file1','w')
f.write('This is anusree\n')
f.write('hello world\n')
f.close()

#################################
#To write something other than string needs to be converted to string first
f=open('file1','a')
value=('The answer is: ', 42)
s=str(value)
f.write(s)
f.close() 


