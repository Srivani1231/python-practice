text=input("enter a word:")
letter=input("enter a character:")
count=0
for ch in text:
    if ch==letter:
        count+=1
print("count=",count)
