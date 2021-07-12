# 11. Write a Python program to find the sequences
# of one upper case letter followed by lower case letters?
import re
x="[A-Z][a-z]"
r="aa Sbc aba aaaaaa aaa a"
matcher=re.finditer(x,r)

for match in matcher:
    print(match.start())
    print(match.group())