
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    
    for ch in s:
        if ch.isalpha():  # only letters
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    
    return v_count, c_count

# Example
text = "Python Programming"
v, c = count_vowels_consonants(text)
print("Vowels:", v, "Consonants:", c)
