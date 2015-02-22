for i, v in enumerate(['tic','tac','toe']):
	print i, v


que = ['name','quest','favourite color']
ans = ['lancelot','the holly grail','blue']
for q,a in zip(que,ans):
	print 'What is your {0} It is {1}. '.format(q,a)



basket = ['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
	print f
