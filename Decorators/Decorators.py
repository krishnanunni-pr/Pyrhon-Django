# adding extra features without changing function definition

def check(func):
    def wrapper(name,age):# ("arjun",16)
        if age<18:
            print("not eligible")
        else:
            return func(name,age)
    return wrapper

@check # calling decorators

def vaccine(name,age):
    print("Eligible for vaccination")

cust_age=int(input("enter age :"))
vaccine("ARJUN",cust_age)