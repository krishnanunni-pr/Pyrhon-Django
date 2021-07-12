# write a code to validate -string starting and ending with a uppercase letter
# -except special characters -minimum length 5 -maximum length 10

import re
str=input("Enter a string :")
x='^[A-Z]\w[A-Z]{5,10}'
match=re.fullmatch(x,str)
if match is not None:
    print("Valid")
else:
    print("invalid")