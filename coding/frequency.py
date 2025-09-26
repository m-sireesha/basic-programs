
def frequency_count(lst):
    freq={}
    for item in lst:
        if item in freq:
            freq[item]+=1
        else:
            freq[item]=1
    return freq

nums=[1,2,2,3,3,3,4,4]
print(frequency_count(nums))