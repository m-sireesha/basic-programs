
def print_diamond(rows):
    # Top half (including middle)
    for i in range(rows):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))
        
    # Bottom half (excluding middle)
    for i in range(rows - 2, -1, -1):
        print(" " * (rows - i - 1) + "*" * (2 * i + 1))

print_diamond(4)

