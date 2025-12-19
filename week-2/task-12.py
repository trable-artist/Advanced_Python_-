import re
sent=input("write a sentence: ")
n_sent=re.findall(r"\b\w+I\b",sent)
print(n_sent)

