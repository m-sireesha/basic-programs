
def split_word_manual(text):
    words=[]
    word=""
    for ch in text:
        if ch.isalpha():
            word+=ch
            
        else:
            if word !="":
                words.append(word.lower())
                word=""
    if word !="":
        words.append(word.lower())
    return words

def freq_count(text):
    words=split_word_manual(text)
    freq={}
    for ch in words:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    return freq

text="python is simple.python is powerful"
print(freq_count(text))
