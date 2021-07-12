#       *
#      * *
#     * * *
#    * * * *

n=int(input("enter the number of levels:"))

for i in range(1,n):
    print(" " * (n- i),end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()
