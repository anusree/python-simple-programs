#Largest number in a list 
number = -1
for i in [2,105,54,41,78,63,95,42,11]:
	if i > number:
		number = i
print "The largest number in the list is:",number

#########################################################
#Smallest number in a list
number = None
for i in [2,105,54,41,78,63,95,42,11]:
	
	if number is None:
		number = i
	elif number > i:
		number = i
print"The smallest number in the list is:",number

#########################################################
#Counting the list
count = 0
for i in [2,105,54,41,78,63,95,42,11]:
	count = count + 1
print "The list contains",count,"numbers"

#########################################################
#Summing the list
result = 0
for i in [2,105,54,41,78,63,95,42,11]:
	result = result + i
print "Sum of the elements is:",result

#########################################################
#Avarage of the list
result = 0.0
count = 0.0
for i in [2,105,54,41,78,63,95,42,11]:
	count = count + 1
	result = result + i
avarage = result /count
print "The avarage of the list is:",avarage
