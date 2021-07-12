import re
x= "[0-9]" # check digits
matcher=re.finditer(x,"1ZX4") #check digits

for match in matcher:
    print(match.start())
    print(match.group())
