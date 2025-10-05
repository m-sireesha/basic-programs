
class Employee:
    def __init__(self):
        self.ename="siri"
        self.eno=100
        self.esal=6000
    
    def emp(self):
        self.edept="hr"
        
e=Employee()
print(e.__dict__)
print()
e.emp()
e.eaddr="USA"
print(e.__dict__)