
class P:
    def __init__(self):
        print("parent constructor")
        
class C(P):
    def __init__(self):
        print("child constructor")
        
c=C()