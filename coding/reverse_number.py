
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10        # get last digit
        rev = rev * 10 + digit  # build reversed number
        num = num // 10         # remove last digit
    return rev

# Example
print(reverse_number(12345))  # Output: 54321
