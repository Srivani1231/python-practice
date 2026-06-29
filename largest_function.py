def large(a,b):
    if a>b:
        return a
    else:
        return b
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
result = large(num1,num2)
print("largest=",result)