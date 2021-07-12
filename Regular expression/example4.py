# check string starting with a and ending with b

import re
n =input("Enter a string :")
x= '^a[a-zA-Z]*[0-9]*[^a-zA-Z0-9]*b$'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")
