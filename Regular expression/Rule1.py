import re
x='[abc]' #either a b or c
matcher=re.finditer(x,"acvfgbha")

for match in matcher:
    print(match.start())
    print(match.group())
