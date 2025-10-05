d={}
d[100]="sireesha"
d[200]="sruthi"
d[300]="swathi"
print(d)
print(type(d))
print(d[100])
d[200]="sravani"
print(d)
del d[300]
d[300]="sravs"
d[400]="swathi"
print(d)
print(d.get(100))
print(d.keys())
for k in d.keys():
    print(k)
    
for v in d.values():
    print(v)
    
for k,v in d.items():
    print(k,"-",v)