import math
results=[]
for i in range(1,4):
    a=int(input("write the a side:"))
    b=int(input("write the b side:"))
    hypotenuse=math.sqrt(a**2+b*b)
    results.append(hypotenuse)
max_length=max(results)
min_length=min(results)
print(f"{max_length} is a max length, {min_length} is a min length")
#3-2
sent=input("enter the sentence: ")
n_sent=sent.split()
result=[]
for word in n_sent:
    alphabet=sorted(word)
    new_word="".join(alphabet)
    result.append(new_word)
print(" ".join(result))

