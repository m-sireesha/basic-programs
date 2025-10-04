
def is_armstrong(num):
    n = num
    digits = 0
    temp = n
    
    # Count digits
    while temp > 0:
        digits += 1
        temp //= 10
    
    # Calculate sum of powers
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    
    return total == num

# Example
print(is_armstrong(153))  # True
print(is_armstrong(123))  # False

