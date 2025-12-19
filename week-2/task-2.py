sent=input("write soomething: ")
sent2=sent.replace(":","%")
count=0
for i in sent:
    if i == ":":
        count +=1
if count > 0:
    print(f"here we have {count} ':' symbols")
    print(sent2)
else:
    print("there is no ':'")

