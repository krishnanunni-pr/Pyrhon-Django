list=[1,5,3,551,6,5,358456,1,3,5640,91,22,33,66,5,44,88,55,44,11,22,32,1,65]

def binsearch():
    list.sort()
    print(list)
    ele = int(input("Enter the element :"))
    flag=0
    low = 0
    upp= len(list)-1
    # print upp
    while low <= upp:
        mid = (low+upp)//2
        #print(mid)

        if ele > list[mid]:
            low = mid+1
        elif ele < list[mid]:
            upp = mid-1
        elif ele == list[mid]:
            flag = 1
            break
    if flag == 1:
        print("found")
    else:
        print("not found")
binsearch()