
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a+b

# Example
fibonacci(6)   # 0 1 1 2 3 5
