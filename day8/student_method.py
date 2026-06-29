class Student:
    def __init__(self,name):
        self.name=name
    def display(self):
        print("student name:",self.name)
s1=Student("srivani")
s1.display()