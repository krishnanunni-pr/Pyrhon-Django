import re
x='a*' # count including zero number of a
matcher=re.finditer(x,"ab mm aa abc aaa")

for match in matcher:
    print(match.start())
    print(match.group())
