
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

# Example
print(is_leap_year(2024))  # True
print(is_leap_year(2023))  # False
