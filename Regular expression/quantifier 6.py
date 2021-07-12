import re
x='^a' # checks string is starting with a ,if yes returns else nothing displays
r="aa sbc aba aaaaaa aaa a"
matcher=re.finditer(x,r)

for match in matcher:
    print(match.start())
    print(match.group())