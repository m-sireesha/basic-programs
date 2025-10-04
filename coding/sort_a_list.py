
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

# Example
print(bubble_sort([5, 3, 8, 6, 2]))  # [2, 3, 5, 6, 8]
