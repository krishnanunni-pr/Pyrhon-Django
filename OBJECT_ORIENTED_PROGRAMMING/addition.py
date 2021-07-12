class Addition:
    def setval(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printval(self):
        print("SUM =",self.num1+self.num2)

add=Addition()
n1=int(input("Enter 1st number :"))
n2=int(input("Enter 2nd number :"))
add.setval(n1,n2)
add.printval()