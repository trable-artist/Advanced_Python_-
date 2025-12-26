#7-1.
import math
def triangle_area(a,b):
    area = (a * b) / 2
    return area

def rectangle_area(a,b):
    area=a*b
    return area

x=int(input("enter the x: "))
y=int(input("enter the y: "))
z=int(input("enter the z: "))
t=int(input("enter the t: "))

result=triangle_area(x,y)+rectangle_area(z,t)
print("the area of quadrilateral equal: ",result)

#7-2.
num=int(input("enter the number: "))
if num>0:
    result=oct(num)
    print(result)
else:
    print("the number is negative")

