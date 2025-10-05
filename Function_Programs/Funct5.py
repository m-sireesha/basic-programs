#using filter() method .syntax :filter(function,sequence)sequence can be list,tuple or string
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1)


l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)