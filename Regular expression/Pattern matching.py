# Pattern matching

# re--- package for pattern matching(re- regular expression)


import re
count=0
matcher=re.finditer("ab","ababababbab") # finditer-used to search for combinationnhere search for combination of ab
print(matcher)# gives position
for match in matcher:
    count+=1
print("COUNT :",count)