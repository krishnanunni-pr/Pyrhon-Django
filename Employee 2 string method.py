class Employee:
    componyname="xyz"
    def __init__(self,emname,id,salary,experiance):
        self.ename=emname
        self.id=id
        self.salary=salary
        self.experiance=experiance

    def printdet(self):
        print(self.ename,self.id,self.salary,self.experiance,Employee.componyname)
    def __str__(self):
        return self.ename+str(self.experiance)
emp=Employee("AMAL",123,123456,10)
print(emp)