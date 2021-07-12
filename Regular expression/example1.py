import re
n ="helloo"
x='\w*'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")