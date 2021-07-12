fixed_amt=10000
wdrw=int(input("Enter withdrawal amount:"))
if wdrw<fixed_amt:
    print("Balance amount is :",fixed_amt-wdrw)
else:
    print("Insufficient balance")