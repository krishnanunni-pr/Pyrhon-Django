a=[1,2,3,4]
b=int(input("ENTER INDEX"))
try:
    print(a[b])
except Exception as e:
    print("exception:",e)