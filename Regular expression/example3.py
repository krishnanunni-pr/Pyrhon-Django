# combination of uppercase and lowercase ending with number

import re
n =input("Enter a string :")
x= '\w+\d$'
match=re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("invalid")