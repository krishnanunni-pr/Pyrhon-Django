#   Minimum and maximum value i n alist

list=[1,2,64,45,5641,32,321,23,31,666]

newlist=[]
min=list[0]

while list:
    min = list[0]
    for i in list:
        if i < min:
            min = i
    newlist.append(min)
    list.remove(min)

print("Minimum element :",newlist[0])
print("Maximum element", newlist[9])