# vaccine: eliglibe or not

age=int(input("Enter your age :"))
if age<18:
    raise Exception("Age below 18 ,:NOT ELIGLIBE")
else:
    print("Eliglibel for vaccination")