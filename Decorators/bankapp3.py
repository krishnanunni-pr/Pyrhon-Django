def login_required(func):
    def wrapper(self,acno,*args,**kwargs):
        if(self,acno)


class Bank:
    users = {
        1000: {"acconu_num": 1000, "password": "user1", "balance": 3000},
        1001: {"acconu_num": 1001, "password": "user2", "balance": 4000},
        1002: {"acconu_num": 1002, "password": "user2", "balance": 5000},
        1003: {"acconu_num": 1003, "password": "user3", "balance": 6000}
    }
    session={}
    def validate_aacount(self,accno):
        if accno in self.users:
            return True
        else:
            return False
    def authenticate(self,**kwargs): #kwargs={acc_no:1000,password:test}

    def balance_enquiry(self,acc_no):
        if(acc_no==self.session["user"]):
            print(self.users[acc_no]["balance"])
        else:
            print("you must login")


# obj=Bank()
# user=obj.authenticate(acc_no=1000,password="user1")
# obj.balance_enquiry(user)

obj1=Bank()
user=obj1.authenticate(acc_no=1000,password="user3")

if (user==-1)|(user==0):
    print("authenrtication failed")
else:
    obj1.balance_enquiry(user)
obj1.fund_transfer(user,1002,5000)



