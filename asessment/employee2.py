f=open("employee","r")
# employees={1000:{"id":1000,"name":"Ajay","desig":"developer","exp":2,"salary":25000}}
employees={}
for line in f:
    eid,name,desig,exp,salary=line.rstrip("\n").split(",")
    employees[int(eid)]={"eid":eid,"name":name,"desig":desig,"exp":exp,"salary":salary}
print(employees)

def printemployee(id=None,**kwargs):
    if id in employees:
        print(employees[id]["name"])
        if "prope" in kwargs:
            if kwargs["prope"] in employees[id]:
                print(employees[id][kwargs["prope"]])
            else:
                print("invalid property")
    else:
        print("invalid id")


printemployee(id=1001,prope="desig")