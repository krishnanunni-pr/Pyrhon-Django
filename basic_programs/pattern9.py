#      *
#     * *
#    * * *
#   * * * *
#  * * * * *


def triangle(n):
    k=6     #print(k)
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")

triangle(5)


#alternative method
n= int(input("Enter the number of levels :"))
for i in range(1,n):
    print(" "*(n-i),end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

