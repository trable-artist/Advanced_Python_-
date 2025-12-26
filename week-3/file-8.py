#8-1.
arr=[]          #use to split and contain the num
result=[]       #only numbers that devideble
num=int(input("enter the number: "))
str_num=str(num)    #we changed to the str cause for do not work with int
for i in str_num:
    arr.append(i)

for j in arr:
    if num%int(j)==0:   #turned j to the int cause we put into arr a str to activate cycle for
        result.append(j)

if len(result)==len(arr):
    print("YES")
else:
    print("NO")
#8-2.
import math
n=int(input("write n: "))
array = list(map(int, input("write numbers: ").split()))
length = int(len(array))
sorted_array=[]
center=int(len(array)/2)
for i in range(len(array)):
        num=array[length-i-1]
        sorted_array.append(num)
print(sorted_array)


