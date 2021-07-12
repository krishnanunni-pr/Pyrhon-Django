import re
x= 'a$' # check ending with a
r="aa sbc ab aaaaak aaa la"
matcher=re.finditer(x,r)

for match in matcher:
    print(match.start())
    print(match.group())