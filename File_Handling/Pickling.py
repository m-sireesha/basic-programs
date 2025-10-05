
import emp,pickle
f=open("emp.dat","wb")
n=int(input("enter no of employees"))
for i in range(n):
    eno=int(input("enter emp number"))
    ename=input("enter emp name")
    esal=float(input("enter emp salary"))
    edept=input("enter emp department")
    e=emp.Employee(eno,ename,esal,edept)
    pickle.dump(e,f)
print("emp objects pickled successfully")