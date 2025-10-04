
def find_max_min(lst):
    if len(lst) == 0:
        return None, None  # handle empty list

    max_val = lst[0]
    min_val = lst[0]

    for num in lst:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val

# Example
numbers = [10, 3, 45, 2, 99, 0]
max_value, min_value = find_max_min(numbers)
print("Maximum:", max_value, "Minimum:", min_value)
