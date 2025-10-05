
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
        
    def display(self):
        print("employee name",self.name)
        print("employee age",self.age)
        print("employee no",self.eno)
        print("employee sal",self.esal)
   
e1=Employee("siri",30,100,6000)
e1.display()
print()
e2=Employee("swathi",40,200,5000)
e2.display()