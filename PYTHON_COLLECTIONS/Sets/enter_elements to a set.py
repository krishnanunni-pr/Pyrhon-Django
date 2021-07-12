# Ask user to enter how many elements wants

set=set()

n=int(input("Enter the number of elements :"))
print("Enter", n, "numbers :")
for i in range (0,n):
    s=int(input())
    set.add(s)
print(set)
