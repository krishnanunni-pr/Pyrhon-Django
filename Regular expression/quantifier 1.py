import re
x='a+'# a including group
matcher=re.finditer(x,"ab aa abc aaa")

for match in matcher:
    print(match.start())
    print(match.group())
