
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch in vowels:
        result += '*'
    else:
        result += ch

print("String after replacing vowels:", result)
