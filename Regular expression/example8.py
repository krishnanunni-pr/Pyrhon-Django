# validate inidan phone numbers

import re
n =input("Enter your phone number:")
x= '[+][9][1]\d{10}$'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")