num1=int(input("Enter a number:"))
num2=int(input("Enter 2nd number:"))
print("Number before swapping :",num1)
print("Number befor swapping:",num2)
(num1,num2)=(num2,num1)
print("after swqpping number 1:",num1)
print("after awapping Number 2:",num2)

7
#method 1
temp=num1
num1=num2
num2=temp

#method 2
(num1,num2)=(num2,num1)

#method 3
num1=num1+num2
num2=num1-num2
num1=num1-num2