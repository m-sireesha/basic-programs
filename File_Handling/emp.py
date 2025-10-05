
class Employee:
    def __init__(self,eno,ename,esal,edept):
        self.eno=eno;
        self.ename=ename;
        self.esal=esal;
        self.edept=edept;
        
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.edept)