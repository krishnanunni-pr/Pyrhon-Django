   #Object Oriented Programming

# class   : design pattern/blueprint
# object  : real world entity
# reference : to perform operations on object


class Person:
    def walk(self):  # method1  #**here funtions is known as methods
        print("Person is Walking")
    def read(self): # method2
        print("Person is reading")
obj1=Person()
obj1.walk()
obj1.read()

obj2=Person()
obj2.walk()
obj2.read()