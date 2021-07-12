# adding extra features without cahnging function definition

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
vaccine("ARJUN",16)