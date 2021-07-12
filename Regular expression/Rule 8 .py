import re
x='\s' #check space
matcher=re.finditer(x,"Av V V")

for match in matcher:
    print(match.start())
    print(match.group())
