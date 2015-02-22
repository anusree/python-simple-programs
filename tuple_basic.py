#list
print "list"
x=[1,2,3]
print x
x[1]=5
print x
#print dir(x)

#tuple
print "tuple..........immutable,can't sort, append,reverse"
y=(1,2,3)
#y[1]=5  it does not possible
print y
#print dir(y)

(x,y)=(4,'fred')
print x, y
(a,b)=(99,1254)
print a , b


#sorting list of tuples
print "SORTING LIST OF TUPLES......"
d={'a' : 10 , 'b' : 22 , 'c' : 14}
print d.items()
t=sorted(d.items())
print t


print "SORT BY VALUES!!!!"
l=list()
for k,v in d.items():
	l.append((v,k))

print l
l.sort(reverse=True)
print l
l.sort(reverse=False)
print l