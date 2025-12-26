import math
print("1:square,2:rectangle,3:triangle,4:circle")
type=input("Enter your type:")
if type=="1":
    length=float(input("write the length of side: "))
    print(f"asnwer is:{length ** 2}")
if type=="2":
    a=float(input("write the length of side a: "))
    b=float(input("write the length of side b: "))
    print(f"asnwer is: {a*b}")
if type=="3":
    a=float(input("write the length of side a: "))
    h=float(input("write the length of side h: ")) #hight
    print(f"asnwer is: {a*h*0.5}")
if type=="4":
    r=float(input("write the radius of circle: "))
    print(f"asnswer is: {(r**2)*math.pi}")
#1-2
import math
array=[[2,5,6],[1,2,3,4],[10,5,3]]
for i in range(len(array)):
    c_array=array[i]
    total=0
    avg=sum(c_array)/len(c_array)
    print(avg,end=' ')
    for j in range(len(c_array)):
        total+=c_array[j]
    print(total)

