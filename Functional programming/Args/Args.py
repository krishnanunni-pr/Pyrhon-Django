# *args

# 1.returns tuple
# 2.can use many arguments in function call

def add(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(2,3,4,5,6,7)