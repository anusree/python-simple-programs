############some definitions############


#1.Name space: Mapping from name to object. eg: the global name in a module, local name in function invocation.	Use the word attribute for any name following a dot. eg: z.real, real is an attribute if object z


#2.Attribute may be read-only or writable. eg: modname.the_answer = 42. Writable attribute may also be deleted with the 'del' statement. eg: 'del modname.the_answer' will remove the attribute 'the_answer' from the object named by 'modname'.

#try this example given bellow
class a:
	"sample class"

aobj=a()
aobj.attir=42
print aobj.attir
del aobj.attir #delete the attribute 'attir' of object 'aobj' using 'del'

#print the ttribute after deleting the attribute it will cause the error that given bellow
#print aobj.attir

#42
#Traceback (most recent call last):
#  File "class_definitions.py", line 16, in <module>
#    print aobj.attir
#AttributeError: a instance has no attribute 'attir'



################################################################
#simple form of class is given bellow

	#class ClassName:
		#<statement-1>
		#.
		#.
		#.
		#<statement-N>



###############################################################
#class object
#class object support two kind of operation: attribute references and instantiation.
#1. Attribute references uses the standard syntax. eg: obj.attribute
#eg:
class MyClass:
	"""A simple example class"""
	i=12345
	def f(self):
		return 'hello world'
#here MyClass.i and MyClass.f are valid attribute references. __doc__ is also valid attribut return the docstring "A simple example class". we can assign value to class attribute so we can change the value of 'MyClass.i'.
#2.Class instatiation uses function notation. eg: 'x=MyClass()' this will create new instance of the class and assign this object to local variable 'x'.


###############################################################
#When a class defines an '__init()__' methode, then the class instantiation automaticaly invoke __init__() for the newly created class instance.
#Eg:
class Complex:
	def __init__(self,realpart,imagpart):
		self.r=realpart
		self.i=imagpart

x=Complex(3.0,4.5)
print x.r,'+',x.i,'i'



