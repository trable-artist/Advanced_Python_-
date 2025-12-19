import re
sent=input("enter the sentence: ")
n_sent=re.findall(r"t",sent)
if n_sent:
    count=len(n_sent)
    print(f"Here we have 't' letter {count} times!")
else :
    print("There is no letter 't'")

