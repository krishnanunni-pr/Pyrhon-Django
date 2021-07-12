str=input("ENTER STRING :")
words=str.split(" ")
dict={}
for i in words:
    count=words.count(i)
    dict.update({i:count})
print(count)