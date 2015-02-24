#factorial
num1 = raw_input("enter the number: \n")
print num1
num2=int(num1)
print type(num2)


def facto(num):
	res=1
	while (num>=1):
		res=res*num
		#print res
		num=num-1
			
	print res


aa=facto(num2)



