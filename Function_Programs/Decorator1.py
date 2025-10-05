
def my_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@my_decorator
def say_hello():
    print("Hello, World!")

say_hello()

'''The @my_decorator is shorthand for say_hello = my_decorator(say_hello)

The wrapper() function adds extra behavior around say_hello()

You can also pass parameters to the wrapped function if needed.'''