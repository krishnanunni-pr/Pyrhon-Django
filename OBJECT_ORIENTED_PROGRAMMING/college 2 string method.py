
class College:
    collegename="ASDFG"

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def printdetails(self):
        print("College name :",College.collegename)
        print("Name : ",self.name)
        print("Roll no : ",self.roll)
    def __str__(self):
        return str(self.roll)+self.name+College.collegename # only prints string ,to print 2 values use string addition
ob=College("anu",25)
print(ob)
ob1=College("alan",36)
print(ob1)
