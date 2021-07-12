
class Person:
    def setval(self,name,age):
        self.name=name  # instasnce variable
        self.age=age
    def printval(self):
        print("Name::",self.name)
        print("age::",self.age)

pe=Person()
n=input("Enter name :")
a=int(input("Enter age :"))
pe.setval(n,a)
pe.printval()