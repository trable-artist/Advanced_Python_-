import re
sent=input("write your sentence: ")
n_sent=sent.replace("!",".")
n_letter=re.findall(r"n+",sent)
num=len(n_letter)
max=0
for i in range(num):
    if max<len(n_letter[i]):
        max=len(n_letter[i])
print(f"The longest sequence of consecutive letters 'n' {max}")
print(n_sent)

