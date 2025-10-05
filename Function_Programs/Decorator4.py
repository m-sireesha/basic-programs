


def decor(func):
    def wrapper1(name):
        print("executing from decor")
        func(name)
    return wrapper1

def decor1(func):
    def wrapper2(name):
        print("executing from decor1")
        func(name)
    return wrapper2    

@decor1
@decor
def wish(name):
    print(f"hello {name} good morning!!!")
    
wish("sireesha")