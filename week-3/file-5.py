#5-1.
import math
A=int(input("write A: "))
B=int(input("write B: "))
C=int(input("write C: "))
D=int(input("write D: "))
first=(A*D)-(C*B)
second=B*D
gcd=math.gcd(first,second)
firts_gcd=first//gcd
second_gcd=second//gcd
result=first/second
print(f"{first}/{second} --> {firts_gcd}/{second_gcd} <--> {result}")
#5-2
num=int(input("enter the number:"))
list=[]
for i in range(1,num+1):
    if num%i==0:
        list.append(str(i))
print("The numbers that devived to the",num,"without remainder:", " ".join(list))

