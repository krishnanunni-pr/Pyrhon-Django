# 8. When is the finally block executed.Explain with example?

num1=int(input("Enter num1 :"))
num2=0

try: # works every time
    print("Hello")
    print(num1/num2)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This is always excecuted")