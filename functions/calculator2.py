def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("SELECT OPERATIONS\n"
        "1:ADDITION\n"
        "2:SUBSTRACTION\n"
        "3:MULTIPLICATION\n"
        "4:DIVISION\n")

while True:
    choice = input("Enter the choice : ")
    if choice in ('1','2','3','4'):
        num1 = float(input("Enter first number :"))
        num2 = float(input("Enter second number : "))
        if choice == '1':
            print(add(num1,num2))
        elif choice == '2':
            print(sub(num1,num2))
        elif choice == '3':
            print(mul(num1,num2))
        elif choice =='4':
            print(div(num1,num2))
        break
    else:
        print("Invalid")