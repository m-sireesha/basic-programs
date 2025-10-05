from sys import argv
print("the number of command line arg",argv)
print("the list of command line args",argv)
print("command line arg one by one ")
for x in argv:
    print (x)
    
print("sum of arg")   
sum=0
args =argv[1:]
for x in args:
     n=int(x)
     sum=sum+n
print("final result",sum)   

       