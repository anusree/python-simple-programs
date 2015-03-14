"""
Consider the following conditional statement.

if p == False:
    return False
elif q == False:
    return False
else:
    return True
That is equivalent to which of the following simpler statements?

Try to reason logically about each of the statements, but also try each in CodeSkulptor.

return (not p) and (not q)
return p and q
return p or q
return (not p) or (not q)
"""




def fun(p, q):
    if p == False:
        return False
    elif q == False:
        return False
    else:
        return True

p = True
q = False
print fun(p,q)

print (not p) and (not q)
print p and q
print p or q
print (not p) or (not q)
