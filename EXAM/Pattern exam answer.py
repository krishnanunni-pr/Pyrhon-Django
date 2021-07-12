a=int(input("Enter initial range :"))
b=int(input("Enter final range :"))
r=int(input("Enter number of rows :"))
for i in range(a,b):
    if(i%2==0):

        for k in range(r, 0, -1):
            for j in range (0, k):
                print(i, end=" ")

            print("\r")

    else:
        for l in range(r):
            for m in range(0,l+1):
                print(i, end=" ")

            print("\r")
