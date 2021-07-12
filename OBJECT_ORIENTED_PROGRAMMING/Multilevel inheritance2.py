# Person parent employee


class Person:
    def prnvalue(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        print(self.name,self.age,self.adrs)
class Parent(Person):
    def ptvalue(self,pname,page,padrs):
        self.padrs=padrs
        self.pname=pname
        self.page=page
        print(self.pname,self.page,self.padrs)
class Employee(Parent):
    def evalue(self,ename,id,comp):
        self.ename=ename
        self.id=id
        self.comp=comp
        print(self.ename,self.id,self.comp)

pa=Parent()
pa.ptvalue("aaa",29,"kmlbodfokv")
pa.prnvalue("BBB",26,"qweqwrwre")

em=Employee()
em.evalue("llll",36,213)
em.ptvalue("ooo",34,"tyui")
em.prnvalue("qqqq",43,"rtrtrty")