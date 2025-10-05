

class Duck:
    def talk(self):
        print("quack quack")
class Dog:
    def bark(self):
        print("bow bow")   
class Human:
    def talk(self):
        print("hello hai...")
        
def f1(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
d=Duck()
f1(d) 

h=Human()
f1(h)   

d=Dog()
f1(d)   

