


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
        acc_no=kwargs["acc_no"]
        password=kwargs["password"]
        user=self.validate_aacount(acc_no)
        if user:
            if (password==self.users[acc_no]["password"]):
                self.session["user"]=acc_no
                return acc_no
            else:
                return -1 # invalid password
        else:

            return 0  # invalid account number

    def balance_enquiry(self,acc_no):
        if(acc_no==self.session["user"]):
            print(self.users[acc_no]["balance"])
        else:
            print("you must login")

    def fund_transfer(self,user,to_acno,amt):
        if self.validate_aacount(to_acno):
            balance=self.users[user]["balance"]
            if balance<amt:
                print("insufficient balance")
            else:
                self.users[user]["balance"]-=amt
                self.users[to_acno]["balance"]+=amt
    def logout(self):
        self.session["user"]=0
# obj=Bank()
# user=obj.authenticate(acc_no=1000,password="user1")
# obj.balance_enquiry(user)

obj1=Bank()
user=obj1.authenticate(acc_no=1001,password="user2")

if (user==-1)|(user==0):
    print("authenrtication failed")
else:
    obj1.balance_enquiry(user)

obj1.fund_transfer(user,1002,2000)
obj1.balance_enquiry(user)
obj1.logout()