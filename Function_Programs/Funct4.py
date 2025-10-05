def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
print("factorial of 4 is :",factorial(4))
print("factorial of 5 is :",factorial(5))

s=lambda n:n*n
print("square of 4 is ",s(4))
print("square of 5 is ",s(5))

s1=lambda a,b:a+b
print("sum of 10,20 is",s1(10,20))
print("sum of 10,20 is",s1(100,200))

s2=lambda a,b:a if a>b else b
print("biggest number in ",s2(100,20))