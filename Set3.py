s="sireesha"
print('e' in s)
print('e' not in s)

x=input("enter string ")
s=set(x)
v={'a','e','i','o','u'}
d=s.intersection(v)
print("different vowels in ",x,"are",d)