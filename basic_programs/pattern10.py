#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

def triangle(n):
    k=n
    for i in range(n,0,-1):
        for r in range(0,k):
            print(end=" ")
        k= k+1
        for j in range(0,i):
            print("* ",end="")
        print("\r")
triangle(5)