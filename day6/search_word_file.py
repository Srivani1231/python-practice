file=open("sample.txt","r")
data=file.read()
word=input("enter word to search:")
if word in data:
    print("word found")
else:
    print("word not found")
file.close()