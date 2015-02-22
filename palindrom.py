a=raw_input("enter the variable: \n")
print a
l=len(a)
print l
l1=l-1
print l1
l2=int(l/2)
print l2
i=0
status=True
while(i<=l2):
	if a[i]==a[l1]:
		i=i+1
		l1=l1-1
	
	else:
		status=False
		break
	
	
if status:
	print "yes"
else:
	print "No"



