list=[10,23,30,13,50,61,70,1,2,3,4,]
print(list)
print(list[0])
print(list[3])
print(list[-1])
list1=list[2:7:1]
print(list1)

list[1]=100
print(list)

print("from while loop")
i=0
while i<len(list):
    print(list[i])
    i=i+1
print("from for loop")
for x in list:
    print(x)
    
print("printing even numbers")
for x in list:
    if x%2 ==0:
        print(x)
    