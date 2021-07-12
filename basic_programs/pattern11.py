#          * * * * * *
#         * * * * * * *
#        * * * * * * * *
#       * * * * * * * * *
#      * * * * * * * * * *




def trapezoid(n):
    k=6     #print(k)
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+6):
            print("*",end=" ")
        print("\r")
trapezoid(6)