# 1. Create a child class Car that will inherit all
# of the variables and methods of Vehicle class?


class Vehicle():
    def vdetails(self,model,type,regno):
        self.model=model
        self.type=type
        self.regno=regno
        print(self.model,self.type,self.regno)
class Car(Vehicle):
    def cdetails(self,brand,price,year):
        self.brand=brand
        self.price=price
        self.year=year
        print("Brand :",self.brand)
        print("price :",self.price)
        print("Year :",self.year)
        print(self.model, "reg no", self.regno)


ca=Car()
ca.vdetails("civic","car","KL45P4563")
ca.cdetails("honda",1236547,2018)


