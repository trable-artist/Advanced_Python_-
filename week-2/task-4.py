sent=input("write soomething: ")
new_sent=sent.replace("a","o").replace("A","O")
count=sent.count("a")
sentl=len(new_sent)
if count > 0:
    print(f"The number of replacement: {count}")
    print(new_sent)
    print(sentl)
else:
    print("There is no 'a' letter in the sentence")
    print(sentl)

