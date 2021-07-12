# User defined exception handling
no1=int(input("Enter a number :"))
no2=int(input("Enter 2nd number :"))
if no1==no2:
    raise Exception("2 Numbers are same ") #user defined exception
else:
    print(no1+no2)