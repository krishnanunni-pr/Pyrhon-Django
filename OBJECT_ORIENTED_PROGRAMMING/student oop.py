class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark


    def printval(self):
        print("Name :",self.name)
        print("Roll no :",self.rollno)
        print("Course :",self.course)
        print("Mark :",self.mark)
    def __str__(self):
        return self.name+self.rollno+self.course+self.mark
f=open("student","r")
for line in f:
    #print(line)
    data=line.rstrip("\n").split(",")
    #print(data)
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=data[3]
    ob=Student(name,rollno,course,mark)
    #print(ob)
    ob.printval()
