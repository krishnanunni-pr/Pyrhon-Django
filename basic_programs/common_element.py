a="abcdefg"
b="xvyt"
c=""
for i in a:
    if i in b:
     c=c+i
if c=="":
    print("no common ")
else:
    print(c)