
def find_missing_number(arr):
    n = len(arr) + 1       # total numbers including missing one
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example
arr = [1, 2, 4, 5, 6]
missing = find_missing_number(arr)
print(f"Missing number is: {missing}")
