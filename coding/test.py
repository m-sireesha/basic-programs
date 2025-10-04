
# def reverse_number(num):
#     rev=0
#     while num>0:
#         digit=num%10
#         rev=rev*10+digit
#         num=num//10
#     return rev
# print(reverse_number(12345))

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

def freq_count_manual(text):
    words=split_word_manual(text)
    freq={}
    for w in words:
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1
    return freq

paragraph="Python is simple. python is powerful"
print(freq_count_manual(paragraph))
        
                
            