# 7. Create a valid phone numbers file from the following file? +915678905432 +914567890321 765432167 123450987765 +919976532456

import re
rule= '[+][9][1]\d{10}$'
f=open("phonenum","r")
f1=open("validnum","w")
for num in f:
     number= num.rstrip(" ")
     matcher = re.fullmatch(rule, number)
     if matcher!=None:
         f1.write(num)
