# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def pattern(row):
    num=1
    for i in range(0,row):
        num=1
        for j in range(0,i+1):
            print(num,end=" ")
            num=num+1

        print("\r")

pattern(5)