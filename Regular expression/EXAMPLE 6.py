# Starting with uppercase followed by lower case,digits symbols single elemenyt is not allowed

import re
n =input("Enter a string :")
x= '[A-Z]{1}[a-zA-Z0-9\W]+'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")
