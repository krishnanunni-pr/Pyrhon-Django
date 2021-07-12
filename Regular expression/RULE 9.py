import re
x='\d' #check the digits
matcher=re.finditer(x,"Av V V123")

for match in matcher:
    print(match.start())
    print(match.group())
