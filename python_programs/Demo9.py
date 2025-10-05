n = int(input("Enter number of rows:"))
for i in range(1,n+1):
   for j in range(1,i+1):
       print("*",end=" ")
   print()
   
   
   
cart=[10,20,600,40,30]
for item in cart:
    if item>50:
        print("to place this order insurance is required")
        break
    print(item)