word=input("write the word: ")
inside=False
new_sentence=""
for i in word:
    if i == "(":
        inside=True
        continue
    elif i==")":
        inside=False
    if inside == True:
        new_sentence+=i
print(new_sentence)

