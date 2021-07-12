def revert_val(func):
    def wrapper(no1,no2):
        if no1<no2:
            (no1,no2)=(no2,no1) # wrapper is common, can change , no of parameters must be same
            return func(no1,no2)
        else:
            return func(no1,no2)
    return wrapper

@revert_val
def sub(num1,num2):
    return num1-num2
print(sub(1,16))
