
def sort_list(nums, descending=False):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] > nums[j] and not descending) or (nums[i] < nums[j] and descending):
                nums[i], nums[j] = nums[j], nums[i]
    return nums

# Example usage
numbers = [5, 2, 9, 1, 5, 6]
print("Ascending:", sort_list(numbers.copy(), descending=False))
print("Descending:", sort_list(numbers.copy(), descending=True))