
from zipfile import *
import os
print(os.getcwd())
f=ZipFile("files.zip","w",ZIP_DEFLATED)
f.write("abc.txt")
f.write("abcd.txt")
f.close()
print("files.zip file created")

f = ZipFile("files.zip", "r",ZIP_STORED)
names =f.namelist()
for name in names:
    print("filename",name)
    print("content of file is")
    f1=open(name,"r")
    print(f1.read())
    print()
f.close()