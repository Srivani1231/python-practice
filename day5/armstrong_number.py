num=int(input("enter a number:"))
original=num
total=0
while num>0:
    digit=num%10
    total+=digit**3
    num=num//10
if total==original:
    print("armstrong number")
else:
    print("not ")