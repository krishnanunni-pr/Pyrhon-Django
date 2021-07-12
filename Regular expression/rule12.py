import re
x='\W' #for special characters
matcher=re.finditer(x,"#$%Av V V")

for match in matcher:
    print(match.start())
    print(match.group())
