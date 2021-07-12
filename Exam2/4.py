# 4.Create an Person class using constructor and build a child class for Employee?

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printper(self):
        print("Name :",self.name)
        print("Age :",self.age)

class Employee(Person):
    def __init__(self,empid,comp,salary,name,age):
        super().__init__(name,age)
        self.comp=comp
        self.salary=salary
        self.empid=empid
    def printemp(self):
        print("Employee id :",self.empid)
        print("Compony name :",self.comp)
        print("salary :",self.salary)

em=Employee(123,"abc compony",123456789,"ARJUN",29)
em.printper()
em.printemp()