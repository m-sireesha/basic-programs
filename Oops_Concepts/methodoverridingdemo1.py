
class P:
    def property(self):
        print("gold+land+cash+power")
    def marry(self):
        print("appalam")
class C(P):
    def marry(self):
        super().marry()
        print("katrina kaif")
        
c=C()
c.property()
c.marry()
