
#positional arguments:
def sub(a,b):
    print(a-b)
sub(100,500)
sub(500,100)

print()
#keyword arguments:
def wish(name,msg):
    print("hello",name,msg)
wish(name="sireesha",msg="how are you!!")
wish(msg="from python",name="siri")
wish("sravs",msg="good morning")
#wish(name="swathi","good bye")error:Positional argument cannot appear after keyword arguments


print()
#default arguments:
def wish(name="guest"):
    print("hello",name,"welcome to python")
wish()
wish("sireesha")


print()
#variable length arguments:
def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("sum = ",total)
sum()
sum(10,20)
sum(10,20,30,40)

#we can mix variable length arg with positional arg
def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)
f1(10)
f1(10,20,30)
f1(10,"A",30,"B")

print()
def f2(*s,n1):
    for s1 in s:
        print(s1)
    print(n1)
f2("A","B",n1=10)
#f2("a","b",10)error variable length arg followed by keyword arg

print()
def display(**kwarg):
    for k,v in kwarg.items():
        print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rollno=100,name="sireesha",subject="java")