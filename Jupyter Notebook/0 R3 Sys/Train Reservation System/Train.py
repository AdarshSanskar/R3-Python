from Person import Person

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
