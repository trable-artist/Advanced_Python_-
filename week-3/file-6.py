
lst = ["a", "abcd", "abc"]

max_len = 0
for s in lst:
    if len(s) > max_len:
        max_len = len(s)

res = []
for s in lst:
    new_s = s + "_" * (max_len - len(s))
    res.append(new_s)

print(res)
