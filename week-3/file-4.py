import math
A=int(input("write A: "))
B=int(input("write B: "))
C=int(input("write C: "))
D=int(input("write D: "))
first=A*D
second=B*C
gcd=math.gcd(first,second)
firts_gcd=first//gcd
second_gcd=second//gcd
result=first/second
print(f"{first}/{second} --> {firts_gcd}/{second_gcd} --> {result}")
#4-2
import math

def check(x,y,a,b,r2):
    location=(x-a)**2 + (y-b)**2
    if location<r2:
        return True
    else: return False

a=int(input("write a:"))
b=int(input("write b:"))
r=int(input("write r:"))
r2=r**2

point=[]
for i in range(3):
    x=int(input(f"write x for {i+1} point:"))
    y=int(input(f"write y for {i+1} point:"))
    point.append([x,y])
count=0
for p in point:
    if check(p[0],p[1],a,b,r2):
        count+=1
        print(f"{p[0]},{p[1]} is in circle")

if count==0:
    print("there is no point in circle")

