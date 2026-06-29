student={
    "name":"srivani",
    "age":20,
    "branch":"ece"
}
key=input("enter key:")
if key in student:
    print(student[key])
else:
    print("key not found")