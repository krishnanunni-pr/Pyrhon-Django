sett={12,2,3,5,7,4,56,32,21,27,33,39,99}
prime=set()
nonprime=set()
for i in sett:
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                nonprime.add(i)
                break
        else:
            prime.add(i)

print("prime set =",prime)
print("non prime = ",nonprime)