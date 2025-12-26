import math

hexagon=int(input("write the a side of hexagon: "))
formula_h=(hexagon**2)*(math.sqrt(3)/4) * 6 #here * to 6 cause of through the area of triangle find the area of h
print(formula_h)

print("Write the sides of triangles: ")
results=[]
for i in range(0,3):
    num=i+1
    a=int(input(f"{num} triangle's a side: "))
    b=int(input(f"{num} triangle's b side: "))
    area=a*b
    results.append(area)
for i in range(len(results)):
    num=i+1
    print(f"The {num} triangle's area is: {results[i]}")

