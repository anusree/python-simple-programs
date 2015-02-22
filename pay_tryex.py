try:
	inhr = raw_input("Enter the houres: ")
	hours = float(inhr)
	inrt = raw_input("Enter the rate: ")
	rate = float(inrt)

except:
	print "Please enter numeric input"
	quit()

if hours <=40:
	pay = hours * rate
	#print pay
else:
	pay = 40 * rate + ( rate * 1.5 * ( hours - 40 ) )
	#print pay
print pay