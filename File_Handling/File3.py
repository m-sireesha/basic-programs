
f=open("abcd.txt","w")
list=["sireesha\n","swathi\n","sravs\n","sruthi\n"]
f.writelines(list)
print("list of lines successfully written to file")
f.close()