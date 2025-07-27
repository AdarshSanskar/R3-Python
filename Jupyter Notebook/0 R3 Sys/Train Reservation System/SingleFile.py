class Person:
    def __init__(self):
        self.name = input("Enter Passenger Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def get_details(self):
        print("Passenger Name :", self.name)
        print("Age            :", self.age)
        print("Gender         :", self.gender)


class Train(Person):
    def __init__(self):
        super().__init__()
        print("-------- Train Booking Section --------")
        self.source = input("Enter Source Station: ")
        self.destination = input("Enter Destination Station: ")
        print()


class ExpressTrain(Train):
    def book_ticket(self):
        print("---------- EXPRESS TRAIN ----------")
        print("Train Type    : Express")
        print("Fare          : ₹250")
        print("Facilities    : Sleeper + Pantry")
        print("From {} to {}".format(self.source, self.destination))
        super().get_details()


class LocalTrain(Train):
    def book_ticket(self):
        print("---------- LOCAL TRAIN ----------")
        print("Train Type    : Local")
        print("Fare          : ₹50")
        print("Facilities    : General seating only")
        print("From {} to {}".format(self.source, self.destination))
        super().get_details()


class SuperFastTrain(Train):
    def book_ticket(self):
        print("---------- SUPERFAST TRAIN ----------")
        print("Train Type    : Superfast")
        print("Fare          : ₹400")
        print("Facilities    : AC + Sleeper + Pantry")
        print("From {} to {}".format(self.source, self.destination))
        super().get_details()
wha

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
