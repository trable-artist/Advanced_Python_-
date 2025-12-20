import re
sent = input("write soomething: ")
new_sent=re.findall(r"[A-Za-z]+" , sent)
length=len(new_sent)
print(length)

