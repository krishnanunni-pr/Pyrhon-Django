class Calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add(self):
        print("SUM = ",self.num1+self.num2)

    def sub(self):
        print("After substraction =",self.num1-self.num2)

    def mul(self):
        print("Prouduct = ",self.num1*self.num2)

    def div(self):
        print("After division = ",self.num1/self.num2)

print("SELECT OPERATIONS\n"
        "1:ADDITION\n"
        "2:SUBSTRACTION\n"
        "3:MULTIPLICATION\n"
        "4:DIVISION\n")
num=int(input("ENTER CHOICE :"))
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
obj=Calculator(a,b)
if num==1:
    obj.add()
elif num==2:
    obj.sub()
elif num==3:
    obj.mul()
elif num==4:
    obj.div()
else:
    print("Enter between given choice")

