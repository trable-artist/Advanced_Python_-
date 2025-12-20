word= input("enter the word: ")
word2=word.split()
num=0
for i in word2:
    if i.lower().startswith("е"):
        num +=1


if num > 0:
    print(f"there have {num} letter 'e'")
else:
    print("there is no letter 'e")

