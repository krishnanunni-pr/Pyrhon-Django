# ****
#  ****
#   ****
#    ****

row=int(input("Enter number of rows : "))
column=int(input("Enter number of columns :"))

for i in range(0, row):
    for j in range(1, i+1):
        print(" ", end="")
    for j in range(0, column):
        print("*", end="")
    print()
