

def second_largest(nums):
    if len(nums) < 2:
        return None

    largest = nums[0]
    second = None

    for x in nums[1:]:
        if x > largest:
            second = largest
            largest = x
        elif x != largest and (second is None or x > second):
            second = x

    return second

# Example
print(second_largest([5, 1, 4, 2, 3]))  # ➞ 4
