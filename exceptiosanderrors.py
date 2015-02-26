##############Errors and Exceptions##############
#syntax error: also known as parsing error
#eg:
	#while True print 'hello world'
	#the error will be like this
	#  File "error_exception.py", line 4
	#    while True print 'hello world'
	#                   ^
	#SyntaxError: invalid syntax
#while True: print 'hello world'


##################Exception####################
#exception: if a statement or expression is syntactically correct, it may cause an error at the time of execution. Errors detected during execution are called exceptions
#some of the error messages are shown here

#1:   print 10 * (1 / 0) 
		#Traceback (most recent call last):
  		#  File "errors_exception.py", line 16, in <module>
    		#    print 10 * (1 / 0) 
		#ZeroDivisionError: integer division or modulo by zero

#2:   print 4+spam*3
		#Traceback (most recent call last):
		#  File "errors_exception.py", line 22, in <module>
		#    print 4+spam*3
		#NameError: name 'spam' is not defined

#3:   print '2' + 2
		#Traceback (most recent call last):
		#  File "errors_exception.py", line 29, in <module>
		#    print '2' + 2
		#TypeError: cannot concatenate 'str' and 'int' objects


#exception are in different type and that tpe are shown in the error messages. eg: ZeroDivisionError, NameError, TypeError


#######################################################3
#Exception Handling: Possible to write program to handle exception. eg is given below:

while True:
	try:
		x=int(raw_input("Please enter a number: "))
		print x," is a valid number"
		break
	except ValueError:
			print "Oops! That was no avalid number.   Try again..."
#output:
#anusree@anusree-Inspiron-5547:~/anusree/python_examples$ python errors_exception.py
#Please enter a number: anu
#Oops! That was no avalid number.   Try again...
#Please enter a number: hai
#Oops! That was no avalid number.   Try again...
#Please enter a number: 42
#42  is a valid number

#A 'try' statement may have more then one 'except' clause to specify handler for different exception.

def this_fails():
	x=1/0
try:
	this_fails()
except ZeroDivisionError as details:
	print 'Handling run-time error', details

####Raising Exception####
#The raise statement allows the programmer to force a specified exception to occur. Examples given bellow:
	#>>> raise NameError('HiThere')
	#Traceback (most recent call last):
	#  File "<stdin>", line 1, in <module>
	#NameError: HiThere




