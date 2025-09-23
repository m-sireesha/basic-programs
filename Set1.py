s={10,20,30}
print(s)
print(type(s))
s.add(40)
s.add(50)
print(s)


l=[10,10,20,30,40,20,50,60,40]
set=set(l)
print(l)
print(set)

s.update(l,range(0,5))
print(s)
print(s.pop())
print(s.pop())
s.remove(50)
#s.remove(100) gives error bcaz ele is not present
s.discard(100)#ele is not present but don't show error
print(s)
s.clear()
print(s)