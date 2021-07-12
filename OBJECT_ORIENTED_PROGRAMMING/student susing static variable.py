# using static variable

class Student:
    schoolname="ABC SCHOOL"
    def setval(self,name,age,rollno,mark):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.mark=mark

    def printval(self):
        print("Name",self.name)
        print("Age",self.age)
        print("Roll no : ",self.rollno)
        print("Mark : ",self.mark)
        print("School name : ",Student.schoolname)

stu=Student()
stu.setval("RAJ",15,22,56)
stu.printval()