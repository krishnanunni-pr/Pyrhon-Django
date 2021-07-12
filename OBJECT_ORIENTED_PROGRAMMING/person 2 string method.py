class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printvalue(self):
        print("Name :",self.name)
        print("Age :",self.age)

    def __str__(self):
        return self.name
f=open("person", "r")
for line in f:
    #print(line)
    data=line.rstrip("\n").split(",")
    #print(data)
    name=data[0]
    age=data[1]
    obj=Person(name,age)
    print(obj)
    obj.printvalue()
