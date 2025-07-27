from Movie import Movie
from Snacks import Snacks

class Amount(Snacks):
    def __init__(self):
        super().__init__()

    def displayAmount(self):
        self.display()
        print("-----------------------------------------------")
        print("--------------Total Amount Payable-------------")
        self.totalAmount = self.ticketPrice + self.snacksPrice + self.seatCharges
        print("Amount : {}".format(self.totalAmount))
        print("-----------------------------------------------")