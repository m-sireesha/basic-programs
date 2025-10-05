
import os,sys
print(os.getcwd())
print(os.listdir())
fname=input("enter file name:")
if os.path.isfile(fname):
    print("file exists:",fname)
    f=open(fname,"r")
else:
    print("file not exists:",fname)
    sys.exit(0)
    
print("contents of file :")
text=f.read()
print(text)