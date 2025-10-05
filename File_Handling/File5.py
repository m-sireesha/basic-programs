
f=open("abcd.txt","r")
print(f.read(5))
print(f.readline())
print(f.read(4))
print("print remaining data")
print(f.read())
f.close()