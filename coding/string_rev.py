
def reverse_string(s):
    reverse_str = ""  
    index = len(s) - 1
    while index >= 0:
        reverse_str += s[index]
        index -= 1
    return reverse_str


text = "Python"
print(reverse_string(text))  

   