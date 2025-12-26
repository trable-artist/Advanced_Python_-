s = input().strip()

if s[0] == 'x':
    b, c = int(s[2]), int(s[4])
    if s[1] == '+':
        print(c - b)
    else:
        print(c + b)

elif s[2] == 'x':
    a, c = int(s[0]), int(s[4])
    if s[1] == '+':
        print(c - a)
    else:
        print(a - c)

elif s[4] == 'x':
    a, b = int(s[0]), int(s[2])
    if s[1] == '+':
        print(a + b)
    else:
        print(a - b)
