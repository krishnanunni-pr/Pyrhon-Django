s={1,2,5,64,4541,3,38,7,3,4,65,3,5,232,11,21,42,8,53,12,46,98}
setodd=set()
seteven=set()

for i in s:
    if i%2==0:
        setodd.add(i)
    else:
        seteven.add(i)
print("Odd =", setodd)
print("Even =", seteven)
