t=(10,20,30,40,50)
print(t)
print(type(t))

list =[60,70,80,90,100]
x=tuple(list)
print(x)
print(type(x))
print(t[0])
print(t[2:5])
#t[1]=200 error bcaz tuple is immutable
print(len(x))
print("packing")
a=10
b=20
c=30
t1=a,b,c
print(t1)
print(type(t1))
print("unpacking")
t=(10,20,30)
a1,a2,a3=t
print("a1=",a1,"a2=",a2,"a3=",a3)

