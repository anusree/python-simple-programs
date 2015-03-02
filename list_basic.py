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


#################################
#List as Stack(last in first out)

	#>>> stack = [3,4,5]
	#>>> stack.append(6)
	#>>> stack.append(7)
	#>>> stack
	#[3, 4, 5, 6, 7]
	#>>> stack.pop()
	#7
	#>>> stack
	#[3, 4, 5, 6]
	#>>> stack.pop()
	#6
	#>>> stack
	#[3, 4, 5]
	#>>> stack.pop()
	#5
	#>>> stack
	#[3, 4]
	#>>> 


#################################
#List as Queues(first in first out)
#To implement a queue, use 'collections.deque' which was designed to have fast appends and pops from both ends.

	#>>> from collections import deque
	#>>> queue = deque(["Eric","John","Michael"])
	#>>> queue.append("Terry")
	#>>> queue.append("Graham")
	#>>> queue
	#deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])
	#>>> queue.popleft()
	#'Eric'
	#>>> queue
	#deque(['John', 'Michael', 'Terry', 'Graham'])
	#>>> queue.popleft()
	#'John'
	#>>> queue
	#deque(['Michael', 'Terry', 'Graham'])
	#>>> 


####################################
#Functional prigramming tools in List
#There are three built-in functions that are very useful when used with lists: filter(), map(), and reduce()

#1) 
#filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true. If sequence is a string or tuple, the result will be of the same type; otherwise, it is always a list.
#eg:

	#>>> def f(x):
	#...     return x%3==0 or x%5==0
	#... 
	#>>> filter(f,range(2,25))
	#[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]
	#>>> 

#2)
#map(function, sequence) calls function(item) for each of the sequence’s items and returns a list of the return values.
#eg:
 
	#>>> def cube(x):
	#...     return x*x*x
	#... 
	#>>> map(cube,range(11))
	#[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
	#>>> 

#More than one sequence may be passed; the function must then have as many arguments as there are sequences and is called with the corresponding item from each sequence
#eg:

	#>>> def add(x,y):
	#...     return x+y
	#... 
	#>>> map(add,range(10),range(10))
	#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
	#>>>

#3)
#reduce(function, sequence) returns a single value constructed by calling the binary function function on the first two items of the sequence, then on the result and the next item, and so on. 
#eg:

	#>>> def add(x,y):
	#...     return x+y
	#... 
	#>>> reduce(add,range(11))
	#55
	#>>> 	
 

