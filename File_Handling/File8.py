
data="All Students are STUPIDS"
f=open("abc.txt","w")
f.write(data)
with open("abc.txt","r+")as f:
    text=f.read()
    print(text)
    print("the current cursor position",f.tell())
    f.seek(17)
    print("the current cursor position",f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text=f.read()
    print("data after modification:")
    print(text)
