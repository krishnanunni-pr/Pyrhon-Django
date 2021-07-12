a=int(input("Enter initial range :"))
b=int(input("Enter final range :"))
row = int(input("Enter the number of rows: "))
num=1
for i in range(a,b):
    for j in range(0, i + 1):
        print(num, end=' ')
    print()

num=num+1
for i in range(row+1,0,-1):
    for j in range(0,i - 1):
        print(num, end=' ')
    print()

num=num+1
for i in range(0,row):
    for j in range(0, i + 1):
        print(num, end=' ')
    print()

num=num+1
for i in range(row+1,0,-1):
    for j in range(0,i - 1):
        print(num, end=' ')
    print()


