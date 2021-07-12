class Employee:
    def setval(self,name,age,cmpnyname,salary):
        self.name=name
        self.age=age
        self.cmpnyname=cmpnyname
        self.salary=salary
    def printval(self):
        print("Name : ",self.name)
        print("age : ",self.age)
        print("company name : ",self.cmpnyname)
        print("salary : ",self.salary)

emp=Employee()
n=input("Enter name :")
a=int(input("Enter age :"))
cmpn=input("Compony name :")
sal=input("salary :")
emp.setval(n,a,cmpn,sal)
emp.printval()