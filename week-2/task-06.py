sent=input("write soomething: ")
new_sent=sent.lower().replace("a","")
sentl=int(len(sent))
new_sentl=int(len(new_sent))
result=sentl-new_sentl
print(f"The number of character was removed: {result}")

