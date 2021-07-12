import re
x= '\D' # except digits
matcher=re.finditer(x,"Av V V")

for match in matcher:
    print(match.start())
    print(match.group())
