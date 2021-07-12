string=input("Enter a string :")
count=0
for i in string:
    if i in "aeiou": # or use variable like v="aeiou",then change if i in v:
        count=count+1
if count==0:
    print("No vowels present")
else:
    print(count)
