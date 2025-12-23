import re

n = int(input())
valid_letters = "ABCEHKMOPTXY"
pattern = f"^[{valid_letters}]\\d{{3}}[{valid_letters}]{{2}}$"

for _ in range(n):
    plate = input().strip()
    if re.match(pattern, plate):
        print("Yes")
    else:
        print("No")
