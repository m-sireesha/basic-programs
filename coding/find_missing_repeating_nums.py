
arr = [1, 2, 3, 4, 4, 5, 6, 6, 8, 10]  # example
n = 10

count = [0] * (n + 1)  # count from 1 to n
for num in arr:
    count[num] += 1

missing = []
repeated = []

for i in range(1, n + 1):
    if count[i] == 0:
        missing.append(i)
    elif count[i] > 1:
        repeated.append(i)

print("Missing numbers:", missing)
print("Repeated numbers:", repeated)
