import math
A=int(input("enter first number"))
B=int(input("enter second number"))
gcd=math.gcd(A,B)
l_gcd=A*B/gcd
print(f"GCD: {gcd}, LCM: {l_gcd}")
#6-2
import math

def get_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

s1 = float(input())
s2 = float(input())
s3 = float(input())
s4 = float(input())
d = float(input())

if (s1 + s2 > d) and (s3 + s4 > d):
    res = get_area(s1, s2, d) + get_area(s3, s4, d)
    print(res)
else:
    print("Error")

