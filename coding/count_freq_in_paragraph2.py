
def split_words_manual(text):
    words = []
    word = ""
    for ch in text:
        # Treat space or punctuation as word separator
        if ch.isalpha():  # only letters are part of a word
            word += ch
        else:
            if word != "":
                words.append(word.lower())  # convert to lowercase
                word = ""
    if word != "":
        words.append(word.lower())
    return words

def word_frequency_manual(text):
    words = split_words_manual(text)
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1 
        else:
            freq[w] = 1
    return freq

# Example
paragraph = "Python is simple. Python is powerful"
print(word_frequency_manual(paragraph))

