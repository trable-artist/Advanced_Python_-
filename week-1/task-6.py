a=int(input("write first number: "))
c=int(input("write second number: "))
b=input("the operation: ")
if b == '-':
    result=a-c
elif b == '+':
    result=a+c
elif b == '/':
    if a == 0:
        print("we cant devide to 0")
        exit()
    else:
        result=a/c
elif b == '*':
    result=a*c
else:
    print("we cant do this")
print("Your result is:", result)

