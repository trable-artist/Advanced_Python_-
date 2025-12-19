sent=input("write a sentence")
split=sent.split()
new_sent=" "
for i in range (len(split)):
    new_sent += split[i].capitalize() + " "
print(new_sent)

second=input("write a second sentence")
print(second.title())

