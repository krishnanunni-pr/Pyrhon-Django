class Student:
    def setval(self,name,age,rollno,mark,schoolname):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.mark=mark
        self.schoolname=schoolname

    def printval(self):
        print("Name",self.name)
        print("Age",self.age)
        print("Roll no : ",self.rollno)
        print("Mark : ",self.mark)
        print("School name : ",self.schoolname)

stu=Student()
stu.setval("RAJ",15,22,56,"GHSS")
stu.printval()