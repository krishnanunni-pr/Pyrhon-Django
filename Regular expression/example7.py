# phone number(10 digits) valid or not

import re
n =input("Enter your phone number:")
x= '[0-9]{10}'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")