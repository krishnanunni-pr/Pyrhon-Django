str = input("Enter a string: ")
vowels="aeiouAEIOU"
flag= ""
for i in str:
   if i not in vowels:
       flag= flag + i

print(flag)