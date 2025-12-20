import re
sent=input("write your sentence: ")
word=input("write your word: ")
n_sent=re.findall('[A-Za-z]+',sent)
count=0
for i in n_sent:
    if i == word:
        count+=1
print(count)

