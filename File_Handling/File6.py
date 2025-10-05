
with open("abc.txt","w")as f:
    f.write("hello \n")
    f.write("from files\n")
    print("file closed?",f.closed)
print("file closed?",f.closed)

