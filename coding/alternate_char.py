
def alternate_chars(s):
    result = ""
    for i in range(0, len(s), 2):
        result += s[i]
    return result

# Example
print(alternate_chars("Python"))  # Output: Pto
