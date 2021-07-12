# Exception handling

# use to solve unexpected errors

# try.....>exceptional code
# except....>solving code/method
# finally....>anything not has importance

num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))
#print(num1/num2) # unexpected error dividong by zero

try: # works every time
    print("Hello")
    print(num1/num2)

except Exception as e: # works only when exception occurs
    print("Exception occured",e)

finally: # works every time
    print("Inside finally")