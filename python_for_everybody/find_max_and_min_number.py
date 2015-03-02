"""5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown."""

max_num = None
min_num = None
while True:
	num = raw_input("Enter a number: ")
	if num == 'done':
		break
        
	try:
		number = int(num)
	except:
		print "Invalid input"
		continue

	if max_num == None or min_num == None:
		max_num = number
		min_num = number
        
	elif number > max_num:
		max_num = number
        
	elif number < min_num:
		min_num = number

print "Maximum is",max_num
print "Minimum is", min_num
