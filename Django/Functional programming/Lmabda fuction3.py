# filter function
# print even numbers only

# filter function - filter(function,iterable) **has condition

lst=[1,2,3,4,5,6,7,8,9] #[2,4,6,8]

even=list(filter(lambda num:num%2==0,lst))# even number
odd=list(filter(lambda num:num%2!=0,lst))
print(even)
print(odd)

