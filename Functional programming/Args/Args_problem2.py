

employees={
    1000:{"eid":1000,"ename":"ajay","salary":123456,"designation":"developer"},
    1001:{"eid":1001,"ename":"arun","salary":546321,"designation":"developer"},
    1002:{"eid":1002,"ename":"shibu","salary":100000,"designation":"analyst"},
    1003:{"eid":1003,"ename":"shyam","salary":124563,"designation":"hr"}
}

# #1 print name of employee whose id is 1002
# print(employees[1002]["ename"])

# #2. print details given by user input

eid=int(input("Enter user id :"))
prop=input("Enter property option eid,ename,salary,designation")

print(employees[eid][prop])