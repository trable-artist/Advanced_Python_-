import math
A=int(input("enter first number"))
B=int(input("enter second number"))
gcd=math.gcd(A,B)
l_gcd=A*B/gcd
print(f"GCD: {gcd}, LCM: {l_gcd}")


