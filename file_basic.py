#searching through a file

fhand = open('file_try.txt','r')
for line in fhand:
	line=line.rstrip()   #strip the new line or white space 
	if line.startswith("saju"):
		print line






#counting the number of lines in a file

fhand1 = open('file_try.txt','r')
count = 0
for line in fhand1:
	count = count+1
print "count: ",count