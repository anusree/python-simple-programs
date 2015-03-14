"""
How many instances of the letter "l" are there in the following:

1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1
Although it might be hard to tell, that string contains ones (1) and lower-case L's (l). Create a small CodeSkulptor program, and use copy-and-paste to put this string in your code. Your program should only need one function or method call.
"""
text = "1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1"
count = 0
print len(text)
def count_l(s1):
    for i in s1:
        global count
        if i == "l":
            count = count + 1
        #print count
    return count
	#print count

print count_l(text)
