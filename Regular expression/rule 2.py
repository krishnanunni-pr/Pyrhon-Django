import re
x='[^abc]' # except abc
matcher=re.finditer(x,"abcsdf1")

for match in matcher:
    print(match.start())
    print(match.group())
