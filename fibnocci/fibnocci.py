x=raw_input("Enter the number:  ")
n=int(x)
a,b=0,1
while(a<n):
	print a
	a,b=b,a+b

print "\n"
a=0
b=1
while(a<n):
	print a
	a=a+b
	b=a-b
		
print "\n"
a=0
b=1
while a<n:
	print a
	c=a+b
	a=b
	b=c
	