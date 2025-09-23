s="sireesha"
print(s)
'''del s
print(s) #error bcaz already deleted s'''

print(s[0])
print(s[1])
print(s[2])
print(s[3])

s1="learning python is easy"
print(s1[1:7:1])
print(s1[7:])
print(s1[::])
print(s1[::-1])

print(len(s))
print(len(s1))


print('e'in s)

print(s1.find("python"))
print(s1.count('s'))
s2=s1.replace('l','e')
print(s2)
print("splitting s1")
l=s1.split()
for x in l:
    print(x)
    
t=("sunny","bunny","funny")
s='-'.join(t)
print(s)