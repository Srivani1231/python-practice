def print_even(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
num=int(input("enter a number:"))
print_even(num)