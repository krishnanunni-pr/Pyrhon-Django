#  First repeating element in a string

pattern=input("Enter a string :")
count={}
for i in pattern:
    if i not in count:
        count.update({i:1})
    else:
        print("First recursive element : ",i)
        break