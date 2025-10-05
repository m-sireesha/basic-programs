
import csv
with open("emp.csv","w",newline='')as f:
    w=csv.writer(f)
    w.writerow(["ENO","ENAME","ESAL","EDEPT"])
    n=int(input("enter no of employees"))
    for i in range(n):
        eno=input("enter emp number")
        ename=input("enter emp name")
        esal=input("enter salary")
        edept=input("enter dept")
        w.writerow([eno,ename,esal,edept])
print("total emp details in csv file")