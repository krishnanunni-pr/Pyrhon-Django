list=[1,2,64,45,5641,32,1,2,321,23,31,666,666]
lst=[]
for i in list:
    if i not in lst:
        lst.append(i)
    else:
        print(i)
