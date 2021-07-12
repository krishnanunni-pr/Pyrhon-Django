# 2 String method

# vehicle class

class Vehicle:
    def vdetails(self,model,compony,regno,colour):
        self.model=model
        self.compony=compony
        self.regno=regno
        self.colour=colour
        print("Model : ",self.model)
        print("Company : ",self.compony)
        print("Reg No : ",self.regno)
        print("Colour : ",self.colour)
    def __str__(self): # 2 string method only one return possible
        return self.model
vh=Vehicle()
vh.vdetails("CIVIC","HONDA","kl123456","black")
print(vh) # gives object location

vh1=Vehicle()