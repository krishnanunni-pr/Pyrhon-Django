import re
x='a{2,3}' # minimum 2 a and maximum 3 a
r="aa sbc aba aaaaaa aaa a"
matcher=re.finditer(x,r)

for match in matcher:
    print(match.start())
    print(match.group())