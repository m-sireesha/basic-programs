
class Duck:
    def talk(self):
        print("quack quack")
class Dog:
    def talk(self):
        print("bow bow")
class Cat:
    def talk(self):
        print("moew moew")    
class Goat:
    def talk(self):
        print("myaah myaah")

def f1(obj):
    obj.talk()
    
l=[Duck(),Cat(),Dog(),Goat()]
for obj in l:
    f1(obj)