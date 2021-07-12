# Inheritance
# single inheritance


class Person(): # Parent class/base class/super class
    def pdetails(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Student(Person): #child class/derived class/sub class
    def sdetails(self,rollno,department,mark):
        self.rollno=rollno
        self.department=department
        self.mark=mark
        print(self.rollno,self.department,self.mark)
        print(self.name,"mark is",self.mark)

st=Student()
st.pdetails("AAA",24,"BBBB")
st.sdetails(1,"cs",86)