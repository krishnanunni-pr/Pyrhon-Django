
lower = int(input("Enter lower range"))
upper = int(input("Enter higher range"))

print("Prime numbers between", lower, "and", upper, "are:")
sum =0
for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           sum=sum+num
print("sum = ",sum)