sent = input("write soomething: ")
print(len(sent))
length = int(len(sent))
n = length // 2
count = 0
new_sent = sent[:n]
for i in new_sent:
    if i == "n":
        new_sent=new_sent.replace("n", "*")
        count += 1
if count > 0:
    print(new_sent)
else:
    print("in first part of sentence has no letter 'n'")

