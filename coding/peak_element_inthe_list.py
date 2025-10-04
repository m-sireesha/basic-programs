
def find_peak(arr):
    n = len(arr)
    
    # Handle edge cases: first or last element can also be a peak
    if n == 1:
        return arr[0]
    if arr[0] >= arr[1]:
        return arr[0]
    if arr[n-1] >= arr[n-2]:
        return arr[n-1]
    
    # Check middle elements
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return arr[i]
    return None

# Example
print(find_peak([1, 3, 20, 4, 1, 0]))  # 20
print(find_peak([10, 20, 15]))         # 20
print(find_peak([5]))                  # 5 (edge case single element)
print(find_peak([10, 5, 2]))           # 10 (peak at start)
