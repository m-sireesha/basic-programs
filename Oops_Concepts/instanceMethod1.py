
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def display(self):
        print("hi",self.name)
        print("your marks are",self.marks)
        
    def grade(self):
        if self.marks>=60:
            print("you got first grade")
        elif self.marks>=50:
            print("you got second grade")
        elif self.marks>=35:
            print("you got third grade")
        else:
            print("you are fail")

n=int(input("enter no of students:"))
for i in range(n):
    name=input("enter name:")
    marks=int(input("enter marks"))
    s=Student(name,marks)
    s.display()
    s.grade()
    print()