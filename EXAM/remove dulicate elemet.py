list=[1,2,64,45,5641,32,1,2,321,23,31,666,666]
lst=[]

[lst.append(i) for i in list if i not in lst]
print(lst)