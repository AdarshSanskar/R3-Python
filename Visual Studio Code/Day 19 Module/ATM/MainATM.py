import ModuleATM as atm
from ModuleATM import username, pin, ch
print("*"*50)
u = input("Enter your Username : ")
p = int(input("Enter your Pin : "))
if p == pin and u == username:
    print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
    ch = int(input("Enter your Choice : "))
    while ch != 4:
        match ch:
            case 1:
                print("*"*50)
                atm.checkBalance()
                print("*"*50)
            case 2:
                print("*"*50)
                atm.deposit()
                print("*"*50)
            case 3:
                print("*"*50)
                atm.withdraw()
                print("*"*50)
            case _:
                print("Incorrect Input")
                
        print("*"*50)
        print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Exit")
        ch = int(input("Enter your Choice : "))
        print("*"*50)
    else:
        print("Thank You for Using ATM, Have a Good Day...")
else:
    print("Incorrect ID or Password")

