#LIST
a=[1,2,3,4,5,6]
b=['a','s','d','f',[1,2,3,]]   #nested list
c=[]
print a,b,c
print 'a' in b
print 'e' in b

#traversing a list
for i in a:
	print i

#compain two list a and b
print a+b    

#list slice
print a[1:4]
print a[:4]
print a[2:]

#list methode
#append() used for add new variable to the list
t1=['a','s','d']
t1.append(2)
print t1
#extend() used for adding the entire list to another list
t2=[1,2,3,4,5]
t1.extend(t2)
print t1


#reduce   compain the sequence of elements and give a single result only for integer values

t=[1,2,3,4]
print sum(t)

#delete an elements pop()in this methode tell the index of the element to be deleted
z=['a','s','d','f','g']
ass = z.pop(2)
print ass
print z
qq=[1,2,3,4,5,6,7,8,9]
#ss=del qq[1]
#print qq
qq.remove(2)
print qq

#convert string to list
print "COVERT STRING TO LIST"
az='spam'
asx=list(az)
print asx

#split a string
print "SPLITTING A STRING"
az='anu is a good girl'
za=az.split()
print za

#sort
print "SORT"
names = ['saju','anu','manu','athira','sanu','smitha']
print names
names.sort()
print names

