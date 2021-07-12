# Person emoloyee class using inheritance and constructors

class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age

    def printval(self):
        print("Name :",self.name)
        print("Age :",self.age)

class Employee(Person):
    def __init__(self,empid,comp,salary,name,age):
        super().__init__(name,age)
        self.comp=comp
        self.salary=salary
        self.empid=empid
    def print(self):
        print("Employee id :",self.empid)
        print("Compony name :",self.comp)
        print("salary :",self.salary)

em=Employee(123,"abc compony",123456789,"akash",28)
em.printval()
em.print()