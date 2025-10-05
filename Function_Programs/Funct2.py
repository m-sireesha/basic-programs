def even_odd(number):
    if number%2==0:
        print("even number")
    else:
        print("odd number")
even_odd(3)
even_odd(10)


def fact(num):
    result =1
    i=1
    while i<=num:
        result=result*i
        i+=1
    print(result)
fact(5)
for i in range(1,6):
    fact(i)
    
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(50,40)
print("sum is",x)
print("sub is",y)