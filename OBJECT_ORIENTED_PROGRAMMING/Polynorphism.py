# Polymorphism....many forms
# overloading..same method name and def num of arguments, python doesnot support overloading
# over-riding


class Operators:
    def num(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print(self.n1+self.n2)
class Display(Operators):
    def num(self,n3):
        self.n3=n3


        print(self.n3)
d=Operators()
d.num(3,8)