# Reduce funtion

from functools import reduce

lst=[1,2,3,4,5,6,7]

# total=reduce(lambda num1,num2:num1+num2,lst)
# print(total)

# highest

# highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
# print(highest)


# another method

result=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(result)