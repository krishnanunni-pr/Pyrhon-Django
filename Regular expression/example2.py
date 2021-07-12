import re
n ='56kg'
x= '[0-9]{2}[a-z]{2}'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")