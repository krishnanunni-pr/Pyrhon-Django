# kerala vehicle registration number validation

import re
n =input("Enter your vehicle registration numberr:")
x= '[K][L][0-9]{2}[A-Z]{1}[0-9]{4}$'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")