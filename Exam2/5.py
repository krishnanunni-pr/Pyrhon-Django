# 5. What is method overriding give an example using Teacher class?


class Teacher:
    def printval(self,name):
        self.name=name
        print("inside parent class",self.name)
class Subject(Teacher):
    def printval(self,subject):
        self.subject=subject
        print("Inside child methods",self.subject)
su=Subject()
su1=Teacher()
su.printval("ASDAS")
su1.printval("asd")
