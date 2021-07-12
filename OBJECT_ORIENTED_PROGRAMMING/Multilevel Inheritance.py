# Multilevel inheritance/hierarchiel


class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def cvalue(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)
class Student(Child):
    def svalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
ch=Child()
ch.cvalue("abc",6)
ch.pvalue("aasdfsdfsds",23)

st=Student()
st.svalue(4,78)
st.cvalue("fdqwe",6)
st.pvalue("aasdaseqwa",25)