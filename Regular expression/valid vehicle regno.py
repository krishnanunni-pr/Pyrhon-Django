import re
rule='[K][L]\d{2}[A-Z]{2}\d{4}$'
f=open("Reg no",'r')
f1=open('validregno','w')
for num in f:
    number=num.rstrip("\n")
    matcher=re.fullmatch(rule,number)
    if matcher!=None:
        f1.write(num)