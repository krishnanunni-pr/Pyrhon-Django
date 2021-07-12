# Inheritance and constuctors in a same program

class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age

    def printval(self):
        print("Name",self.name)
        print("Age",self.age)

class Student(Person):
    def __init__(self,rollno,mark,name,age):
        super().__init__(name,age)
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)

cr=Student(2,56,"ASHA",23)
cr.printval()
cr.print()