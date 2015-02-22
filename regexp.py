import re
print "\nSTRING USING find() METHODE!!!!!\n"
hand = open('file_try.txt')
for line in hand:
	line = line.rstrip()
	if line.find('saju')>=0:
		print line



print "\nREGULAR EXPRESSION USING re.search() METHODE!!!!!!\n"
hand = open('file_try.txt')
for line in hand:
	line = line.rstrip()
	if re.search('saju',line):
		print line

print "\nSTRING USING startswith() METHODE"
hand = open('file_try.txt')
for line in hand:
	line = line.rstrip()
	if line.startswith('anu'):
		print line

print "\nREGULAR EXPRESSION USING re.search() METHODE"
hand = open('file_try.txt')
for line in hand:
	line = line.rstrip()
	if re.search('^cx\S+',line):
		print line
	#print "\nREGULAR EXPRESSION\n"
	if re.search('^cx.*',line):
		print line


x='my 2 favourite number are 19 and 42 AEIOU'
y=re.findall('[0-9]+',x)
print y
y=re.findall('[AEIOU]+',x)
print y
print "GREEDY matching"
x='From: using the: charecter'
y=re.findall('^F.+:',x)
print y
print "NON-GREEDY matching"
x='From: using the: charecter'
y=re.findall('^F.+?:',x)
print y

x="my mail id is anusree.a04@gmail.com saju"
y=re.findall('\S+@\S+',x)
print y