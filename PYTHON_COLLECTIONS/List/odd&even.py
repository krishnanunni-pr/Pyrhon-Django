lst=[1,2,5,64,4541,3,38,7,3,4,65,3,5,232,11,21,42,8,53,12,46,98]
lstodd=[]
lsteven=[]

for i in lst:
    if i%2==0:
        lstodd.append(i)
    else:
        lsteven.append(i)
print("Odd =", lstodd)
print("Even =", lsteven)
