
import emp,pickle
f=open("emp.dat","rb")
print("emp details:")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
    except EOFError:
        print("all emp completed ")
        break
f.close()