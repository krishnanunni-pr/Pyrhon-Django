class Bank:
    def account(self,name,accntno,bname,):
        fixedamnt=100000
        self.name=name
        self.accntno=accntno
        self.bname=bname
        self.minimumbal=10000
        self.balance=self.minimumbal

    def deposit(self,amt):
        self.amt=amt
        self.balance+=self.amt
        print("Your",self.bname,"account has been creadited with amount",self.amt)
        print("Your current balance = ",self.balance)

    def withdraw(self,amnt):
        self.amnt=amnt
        if self.amt>self.balance:
            print("Insufficient balance")
        else:
            print("account debited with",self.amnt)
            self.balance-=self.amnt
            print("Available balance = ",self.balance)

obj= Bank()
num=int(input("Enter account number : "))
obj.account(num,"ABC",'SBI')
obj.deposit(2000)
obj.withdraw(1000)