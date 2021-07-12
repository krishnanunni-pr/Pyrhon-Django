# Remove puctuation from a given string
# punct= punctuatiom
str = input("Enter a string: ")
punct ="!@#$%^&*()_+{}|[]\/;':,.<>?"
flag= ""
for i in str:
   if i not in punct:
       flag= flag + i

print(flag)
