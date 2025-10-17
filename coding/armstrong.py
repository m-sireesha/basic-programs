

def is_armstrong(num):
    # Convert to string to count digits easily
    s = str(num)
    n = len(s)
    
    total = 0
    for ch in s:
        digit = int(ch)
        total += digit ** n
    
    return total == num

# Example usage:
print(is_armstrong(153))  # True, because 1^3 + 5^3 + 3^3 = 153
print(is_armstrong(123))  # False

