# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
#

def pattern(row):
    num=1
    for i in range(0,row):
        for j in range(0,i):
            print(num,end=" ")
            num=num+1


        print("\r")

pattern(6)