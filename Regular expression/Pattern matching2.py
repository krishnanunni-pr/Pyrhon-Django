import re

count=0
matcher=re.finditer("ab","ababbads")

for match in matcher:
    print("Match available at",match.start()) # return positions
    print("Group:",match.group()) #which object find match
    count+=1
print("COUNT :",count)