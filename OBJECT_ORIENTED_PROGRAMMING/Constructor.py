  # # CONSTRUCTOR: to initiate instance variables
  # # constructor automatically invoke when creating the object

class Person():
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printval(self):
        print(self.name,self.age,self.address)

name=input("Enter name :")
pe=Person(name,24,"asdhgjag")
pe.printval()