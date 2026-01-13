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
