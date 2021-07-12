#create a function with arguments and return type which find sum of prime numbers between 1 - 50?

def sumprime(x,y):
    sum = 0
    for num in range(x,y+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:

                sum = sum + num
    return sum


print("Sum of prime numbers from 1 to 50 is : ",sumprime(1,50))
