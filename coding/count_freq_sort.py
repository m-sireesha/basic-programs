
def split_words_manual(text):
    words = []
    word = ""
    for ch in text:
        if ch != " ":       # space separates words
            word += ch
        else:
            if word != "":
                words.append(word)
                word = ""
    if word != "":
        words.append(word)
    return words

def frequency_and_sort_manual(text):
    words = split_words_manual(text)

    # Count frequencies manually using lists
    unique_words = []
    counts = []

    for w in words:
        found = False
        for i in range(len(unique_words)):
            if unique_words[i] == w:
                counts[i] += 1
                found = True
                break
        if not found:
            unique_words.append(w)
            counts.append(1)

    # Combine words and counts into a list
    items = []
    for i in range(len(unique_words)):
        items.append([unique_words[i], counts[i]])

    # Manual bubble sort alphabetically
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][0] > items[j+1][0]:
                items[j], items[j+1] = items[j+1], items[j]

    return items

# Example
text = "zebra lion tiger lion zebra cat"
print(frequency_and_sort_manual(text))
