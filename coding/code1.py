
def remove_duplicate(lst):
    result=[]
    for i in lst:
        if i not in result:
            result.append(i)
    return result
nums=[1,1,2,2,3,4,5]
print(remove_duplicate(nums))