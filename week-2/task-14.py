import re
sent=input("enter the sentence: ")
n_sent=re.findall(r"\ba\w+|\w+i\b",sent)
if n_sent:
    print(f"There we have this words: {n_sent}")
else:
    print("There is no letter starts with 'a' and ends with 'i'")

