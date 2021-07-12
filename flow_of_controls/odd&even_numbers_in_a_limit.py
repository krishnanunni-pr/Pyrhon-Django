low_lmt=int(input("Enter the lower limit :"))
upp_lmt=int(input("Enter the upper limit for range: "))
print("Even numbers between zero and enteredd number are: ")
for i in range(low_lmt,upp_lmt+1):
    if(i%2==0):
        print(i)

print("Odd numbers between zero and entered number are: ")
for i in range(low_lmt,upp_lmt+1):
    if(i%2==1):
        print(i)

