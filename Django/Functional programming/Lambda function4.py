# if num<5 num-1 else num+1

lst=[2,3,4,8,10,7]

below=list(map(lambda num:num+1 if num>5 else (num-1),lst))
print(below)




