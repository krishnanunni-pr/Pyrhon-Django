x=input("enter a string :")
count=0
for i in x:
     count=x.count(i)
     if count > 1:
         break
print("first recursive element is",i)
