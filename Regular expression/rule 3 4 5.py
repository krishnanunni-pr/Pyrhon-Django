import re
x='[a-zA-Z]' # a to z ,A to Z ,both lower and upper case are checked
matcher=re.finditer(x,"ABcdfG") #both lower and upper case checked

for match in matcher:
    print(match.start())
    print(match.group())
