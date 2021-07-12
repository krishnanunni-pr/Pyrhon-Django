import re
x='a{3}' # gives position of combination of number given in curly brace
r="aa sbc aba aaa"
matcher=re.finditer(x,r)

for match in matcher:
    print(match.start())
    print(match.group())