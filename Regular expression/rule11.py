import re
x='\w' #all words except special characters
matcher=re.finditer(x,"#$%Av V V")

for match in matcher:
    print(match.start())
    print(match.group())
