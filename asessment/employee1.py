# emp=open("employee","r")
# list = [(line.strip()).split() for line in emp]
# print(list)

emp = {}
fixed = {}
i = 1
with open("employee", 'r') as f:
    for line in f:
        listDetails = line.strip().split(',')
        fixed[i] = {"id": listDetails[0]}
        fixed[i].update({"name": listDetails[1]})
        fixed[i].update({"role": listDetails[2]})
        fixed[i].update({"number": listDetails[3]})
        fixed[i].update({"salary": listDetails[4]})
        i+=1
print(fixed)

def details(**kwargs):
    id=kwargs["id"]
    name=kwargs["name"]
    role=kwargs["role"]
    number=kwargs["number"]
    salary=kwargs["salary"]
    if id in emp:
        print(emp["id"]["name"])
    else:
        print("invalid id")

details(id=1000)