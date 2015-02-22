purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print purse
print purse['candy']
purse['candy'] = purse['candy']+2
print purse['candy']


#When we see a new name
counts = dict()
names=['anu','saju','manu','smitha','athira','sanu','anu','saju']
for name in names:
	if name not in counts:
		counts[name]=1
	else:
		counts[name]=counts[name]+1
print counts 

a=dict()
print "Enter the line of text: "
#line = raw_input()
line = "anu is good girl good anu saju boy"
print line
words=line.split()
print words
print "counting.......\n"
for word in words:
	a[word]=a.get(word,0)+1 
print a  


a={'anu' : 1 , 'saju' : 2 , 'ammu' : 2 , 'achu' : 1}
for b in a:
	print b, a[b]
print a.keys()
print a.values()
print a.items()
#two iteration variables
for aa,bb in a.items():
	print aa, bb



                                      