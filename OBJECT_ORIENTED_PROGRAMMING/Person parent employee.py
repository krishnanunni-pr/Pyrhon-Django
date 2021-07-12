 # Person Parent Employee


class Person:
    def prnvalue(self,name,age,adrs):
        self.name=name
        self.age=age
        self.adrs=adrs
        #print(self.name,self.age,self.adrs)
class Parent:
    def ptvalue(self,pname,page,padrs):
        self.padrs=padrs
        self.pname=pname
        self.page=page
        #print(self.pname,self.page,self.padrs)
class Employee(Person,Parent):
    def evalue(self,ename,id,comp):
        self.ename=ename
        self.id=id
        self.comp=comp
        print(self.name,self.age,self.adrs)
        print(self.pname, self.page, self.padrs)
        print(self.ename,self.id,self.comp)
obj=Employee()
obj.prnvalue("asda",36,"asdasdasd")
obj.ptvalue("qweqw",29,"qweqqqqqq")
obj.evalue("hgddddd",5656,"cvxdfvx")
