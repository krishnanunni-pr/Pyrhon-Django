class Teacher():
    clgname="ABC COLLEGE"
    def __init__(self,thrname,subject,thrid,dptmt):
        self.thrname=thrname
        self.subject=subject
        self.thrid=thrid
        self.dptmt=dptmt
    def printval(self):
        print("Name :",self.thrname)
        print("Subjecy :",self.subject)
        print("Teacher id :",self.thrid)
        print("Department :",self.dptmt)

obj=Teacher("AA","BBB",1236,"CCCC")
obj.printval()