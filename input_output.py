#There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use.
s='Hello world'
print str(s)
print repr(s)
print str(1.0/7.0)
print repr(1.0/7.0)
x=10*3.25
y=200*200
s='The value of x is: ',repr(x),', and value of y is: ',repr(y),'....'
ss='The value of x is: '+repr(x)+', and value of y is: '+repr(y)+'....'
print s
print ss
# The repr() of a string adds string quotes and backslashes
hello='hello world\n'
hellos=repr(hello)
print hellos
hellos=str(hello)
print hellos
# The argument to repr() may be any Python object
print repr((x,y,('spam','egg')))
#There are two ways to write a table of squares and cubes
#rjust() which right justifes a string similar methods ljust(), center()
for x in range(1,11):
	print repr(x).rjust(2),repr(x*x).rjust(3),
	print repr(x*x*x).rjust(4)
for x in range(1,11):
	print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
#str.zfill(), which pads a numeric string on the left with zeros. It understands about plus and minus signs
print '12'.zfill(4)
print '-3.14'.zfill(8)
# usage of the str.format() 
print 'I am {} he is {}'.format('anusree','saju')
#The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets refers to the position of the object passed into the str.format() method.
print '{0} and {1}'.format('spam','egg')
print 'This {food} is {nice}'.format(food='dinner',nice='incredible')

