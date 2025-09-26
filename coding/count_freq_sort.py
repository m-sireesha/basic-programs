
def frequency_sorted(text):
    words = text.split()
    
    # count frequencies
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1

    # convert dict to list of (word, count)
    items = []
    for k in freq:
        items.append([k, freq[k]])

    # manual bubble sort by word
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][0] > items[j+1][0]:   # compare words
                items[j], items[j+1] = items[j+1], items[j]

    return items

# Example
text = "zebra lion tiger lion zebra cat"
print(frequency_sorted(text))
# Output: [['cat', 1], ['lion', 2], ['tiger', 1], ['zebra', 2]]
