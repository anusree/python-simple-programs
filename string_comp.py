#string comparisson
str1 = raw_input("Enter the first string: \n")
#print str1
str2 = raw_input("Enter the second string: \n")
#print str2
len1 = len(str1)
#print len1
len2 = len(str2)
#print len2
status=True
if (len1!=len2):
	print "Length of the string not same"

i=0
j=0
while (j<len2):
	if (str1[i]!=str2[j]):
		status=False
	i=i+1
	j=j+1

if status:
	print str1+ " and " +str2 +" are same"
else:
	print "String are not same"


