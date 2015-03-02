count = 0
total = 0
while True:
	num = raw_input("Enter a number: ")
	if num == 'done':
		break
	try:
		number = float(num)
	except:
		print "Pleaes, Enter a valid number"
		continue
	count = count + 1
	total = total + number
print count
print total
avg = total / count
print avg
