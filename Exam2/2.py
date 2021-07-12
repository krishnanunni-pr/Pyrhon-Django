# 2. Create an example for three types of inheritance
# in one program by using College as main class?

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
class Student(Person,Child):
    def svalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.rollno,self.mark)
st=Student()
st.pvalue("Amal",22)
st.cvalue("abc",9)
st.svalue(2,66)

pa=Child()
pa.cvalue("thrissur",12)
pa.pvalue("athul",39)


