
def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

# Example
print(remove_duplicates([1, 2, 2, 3, 1, 4, 3]))  # [1, 2, 3, 4]
