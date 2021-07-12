# LOCAL VARIABLE

def printval():
    x=10
    print(x)
printval()
print(x)


# GLOBAL VARIABLE
def printval():
    global x=10
    print(x)
printval()
print(x)