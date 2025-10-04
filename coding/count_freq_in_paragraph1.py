
def word_frequency(paragraph):
    words = paragraph.replace(".", " ").split()  # remove '.' and split
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    return freq

# Example
text = "Python is simple. Python is powerful."
print(word_frequency(text))  
# Output: {'Python': 2, 'is': 2, 'simple': 1, 'powerful': 1}
