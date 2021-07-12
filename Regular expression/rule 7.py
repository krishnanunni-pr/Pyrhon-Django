import re
x= '[^a-zA-Z0-9]' #EXCEPT NUMBERS AND ALPHABETS
matcher=re.finditer( x , "AvAb34#@$BBHKJIaaam") # To find special symbols

for match in matcher:
    print( match.start () )
    print( match.group () )
