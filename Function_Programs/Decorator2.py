
def greet_decorator(funct):
    def wrapper(name):
        print("welcome!!!")
        funct(name)
        print("have a nice day")
    return wrapper


@greet_decorator
def say_name(name):
    print("hello{name}")

say_name("sireesha")
