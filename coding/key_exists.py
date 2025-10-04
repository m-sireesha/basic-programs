
def check_key(d, key):
    if key in d:
        print(d[key])
    else:
        print("Key not found")

# Example
data = {"name": "Alice", "age": 25}
check_key(data, "age")   # Output: 25
check_key(data, "city")  # Output: Key not found
