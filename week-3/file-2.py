a = input().strip()
b = input().strip()

n = len(a)
m = len(b)
double_b = b + b
count = 0

for i in range(n - m + 1):
    substring = a[i:i + m]
    if substring in double_b and len(substring) == m:
        count += 1

print(count)
