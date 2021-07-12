# program to change pin and delete account,if the user is admin only

def admin_required(func):
    def wrapper(user,pin):
        if user!="admin":
            raise Exception("You are not allowed")
        else:
            return func(user,pin)
    return wrapper
@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_acc(user,accno):
    return str(accno)+"delete"
print(change_pin("admin",1000))
print(delete_acc('user1',1000))