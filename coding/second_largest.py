
def second_largest(nums):
    if len(nums) < 2:
        return None
    
    largest = max(nums)
    second = None
    
    for x in nums:
        if x != largest:
            if second is None or x > second:
                second = x
    return second

# Example
print(second_largest([5, 1, 4, 2, 3]))  # 4
