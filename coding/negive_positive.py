
def rearrange_negatives_first(nums):
    negative = []
    positive = []
    for num in nums:
        if num < 0:
            negative.append(num)
        else:
            positive.append(num)
    return negative + positive

# Example usage
arr = [12, -11, -13, -5, 6, -7, 5, -3, -6]
print("Rearranged:", rearrange_negatives_first(arr))