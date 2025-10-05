from functools import*
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)

def wish(name):
    print("good morning ",name)
greeting=wish
print(id(wish))
print(id(greeting))

greeting('sireesha')
wish('siri')