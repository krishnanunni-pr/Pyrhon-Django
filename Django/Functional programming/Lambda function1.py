# Lambda function

# 1. map function - uses when there is no condition
# 2. filter function - used when there is a condition


# Map function
# syntax : map(function,iterables) **do not have condition


# find all square numbers
lst=[1,2,3,4,5,6,7] # DESIRED OUT=[1,4,9,16,25,36,49]
sq=list(map(lambda num:num**2,lst)) # map function
print(sq)