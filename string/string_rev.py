str = raw_input("Enter the string: \n")
l = len(str)
print l
l1 = l-1
str1 = []
i=0

while (l1>=0):

	#Strings are immutable so add that string reverse to list
	str1.append(str[l1]) 
	
	l1=l1-1
print str
print str1
nn="".join(str1)
print nn





