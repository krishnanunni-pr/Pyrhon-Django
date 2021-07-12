list=[1,2,3,0,56,31,25,26,65,36,55,46,43,25,51]
print("Before sorting : ",list)
newlist=[]
min=list[0]

while list:
    min = list[0]
    for i in list:
        if i < min:
            min = i
    newlist.append(min)
    list.remove(min)

print("After sorting : ",newlist)