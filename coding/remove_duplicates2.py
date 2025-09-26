

#remove duplicates with out set()
def remove_duplicate(lst):
    result=[]
    for item in lst:
        if item not in result:
            result.append(item)
    return result

nums=[1,2,2,4,5,5,6,6]
print(remove_duplicate(nums))

