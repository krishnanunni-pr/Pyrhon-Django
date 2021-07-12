print("SELECT OPERATIONS\n"
        "1:ADDITION\n"
        "2:SUBSTRACTION\n"
        "3:MULTIPLICATION\n"
        "4:DIVISION\n")
def add():
    num1=float(input("Enter a number:"))
    num2=float(input("Enter 2nd number:"))
    sum=num1+num2
    print("SUM=",add)
def sub():
    num1=float(input("Enter a number:"))
    num2=float(input("Enter 2nd number:"))
    diff=num1-num2
    print("DIFFERNCE=",diff)
def mul():
    num1=float(input("Enter a number:"))
    num2=float(input("Enter 2nd number:"))
    prdt=num1*num2
    print("PRODUCT=",prdt)
def div():
    num1=float(input("Enter a number:"))
    num2=float(input("Enter 2nd number:"))
    ans=num1/num2
    print("ANSWER IS",ans)

num=int(input("Enter a choice:"))
if num==1:
    add()
elif num==2:
    sub()
elif num==3:
    mul()
elif num==4:
    div()
else:
    print("Enter between given choice")
