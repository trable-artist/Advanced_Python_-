sent=input("write soomething: ")
new_sent=sent.replace(".","")
count=0
for i in sent:
    if i == ".":
        count +=1
if count > 0:
    print(f"here we have {count} '.' symbols")
    print(new_sent)
else:
    print("there is no '.'")

