basket=['apple','orenge','appele','pear','orenge','banana']
print basket
fruit=set(basket)
print fruit
print 'orenge' in fruit
print 'cabbage' in fruit
a='anuanusaju'
aa=set(a)
print aa
b='sajuanuathira'
bb=set(b)
print bb
print "letters in a but not in b ", aa - bb
print "letters in either aa or bb ", aa | bb
print "letters in both aa and bb ", aa & bb
print "letters in aa or bb but not in both ", aa ^ bb
