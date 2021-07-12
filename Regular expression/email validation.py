import re
mail=input("Enter maid id :")
rule='[a-zA-Z0-9]+[@][a-z]+[.][a-z]+'
match=re.fullmatch(rule,mail)
if match is not None:
    print("Valid")
else:
    print("invalid")