from Train import ExpressTrain, LocalTrain, SuperFastTrain

print("===== RAILWAY RESERVATION SYSTEM =====")
print("Select Train Type:")
print("1. Express Train")
print("2. Local Train")
print("3. Superfast Train")
choice = int(input("Enter Your Choice (1/2/3): "))

if choice == 1:
    t = ExpressTrain()
elif choice == 2:
    t = LocalTrain()
elif choice == 3:
    t = SuperFastTrain()
else:
    print("Invalid choice! Booking cancelled.")
    exit()

print()
t.book_ticket()
