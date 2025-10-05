l=[1,2,3,4,5]
def doubleit(x):
    return 2*x
l1=list(map(doubleit,l))
print(l1)

l=[1,2,3,4,5]
l1=list(map(lambda x:2*x,l))
print(l1)
l2=list(map(lambda x:x*x,l))
print(l2)

a=[1,2,3,4]
b=[2,3,4,5]
c=list(map(lambda x,y:x*y,a,b))
print(c)

