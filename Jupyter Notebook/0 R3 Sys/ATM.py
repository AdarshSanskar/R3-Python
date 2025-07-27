class ATM:
    balance = 5000
    def checkBalance():
        global balance
        print(f"Welcome {username}, Yout Balance is : ")
        print("Balance : ", balance)

    def deposit():
        global balance
        amount = int(input("Enter the Amount to Deposit : "))
        balance += amount
        print(f"Successfully Deposited '₹{amount}' to your Account...")
    
    def withdraw():
        global balance
        amount = int(input("Enter the Amount to Withdraw : "))
        if amount < balance:
            balance -= amount
            print(f"Successfully Withdrawed '₹{amount}' from your Account...")
        else:
            print("Insufficient Balance...")
