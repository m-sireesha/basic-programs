
class Student:
    def setName(self,name):
        self.name=name
        
    def getName(self):
        return self.name
    
    def setmarks(self,marks):
        self.marks=marks
        
    def getmarks(self):
        return self.marks

n=int(input("enter no of students:"))
for i in range(n):
    s=Student()
    name=input("enter name:")
    s.setName(name)
    marks=int(input("enter marks"))
    s.setmarks(marks)
    
    print("hi",s.getName())
    print("your marks are",s.getmarks())
    print()