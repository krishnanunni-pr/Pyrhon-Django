# minimum length 8 maximum length 15 except numbers

import re
n =input("Enter a string :")
x= '[\D]{8,15}' # OR [a-zA-Z]\D
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")
