# Over-riding.....same method name and same no of arguments


class Person:
    def printval(self,name):
        self.name=name
        print("inside parent class",self.name)
class Child(Person):
    def printval(self,class1):
        self.class1=class1
        print("Inside child methos",self.class1)
ch=Child()
ch.printval("ASDAS")

# child class method over rides parent classs method