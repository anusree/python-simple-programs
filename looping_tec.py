#When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function
for i, v in enumerate(['tic','tac','toe']):
	print i, v


#To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
que = ['name','quest','favourite color']
ans = ['lancelot','the holly grail','blue']
for q,a in zip(que,ans):
	print 'What is your {0} It is {1}. '.format(q,a)


#To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
	print f

#When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the iteritems() method.
knights = {'hallahad':'the pure','robin':'the brave'}
for k,v in knights.iteritems():
	print k,v
