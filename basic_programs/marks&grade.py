mark1=int(input("Enter the mark:"))
mark2=int(input("Enter the mark:"))
mark3=int(input("Enter the mark:"))
mark4=int(input("Enter the mark:"))
total=mark1+mark2+mark3+mark4
print("The total mark of the person :",total)
avg_mark=total/4
percent=(total/200)*100
print("Average mark : ",avg_mark)

if(percent>=90):
    print("A+ Grade")
elif(80<=percent<90):
    print("A Grade")
elif(70<=percent<80):
    print("B+Grade")
elif(60<=percent<70):
    print("B Grade")
elif(50<=percent<60):
    print("C+ Grade")
elif(40<=percent<50):
    print("C Grade")
elif(30<=percent<40):
    print("D+ Grade")
else:
    print("FAIL")