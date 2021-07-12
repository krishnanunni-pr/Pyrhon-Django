import re
rule= '[+][9][1]\d{10}$'
f=open("mobilenum","r")
for num in f:
     number= num.rstrip("\n")
     matcher = re.fullmatch(rule, number)
     if matcher!=None:
         print(num)

