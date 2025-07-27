from Movie import Movie
class Snacks(Movie):
    snacksPrice = 0.0
    cnt = 0
    def __init__(self):
        super().__init__()
        print("-----------------------------------------------")
        print("------------------Add Snacks-----------------")
        print("1. Diet Coke (₹100)")
        print("2. Sandwich (₹150)")
        print("3. Cheese Popcorn (₹200)")
        print("Enter Zero to Exit : ")
        print("-----------------------------------------------")
        self.cokeCnt = 0
        self.sandwichCnt = 0
        self.popcornCnt = 0
        self.snacks = int(input("Enter Your Choice : "))
        self.coke = " "
        self.popcorn = " "
        self.sandwich = " "
        while self.snacks != 0:
            self.cnt += 1
            match self.snacks:
                case 1:
                    print("Added Diet Coke (₹100)")
                    self.snacksPrice += 100
                    self.cokeCnt += 1
                    self.coke = f"{self.cokeCnt} * Diet Coke (₹100)"
                case 2:
                    print("Added Sandwich (₹150)")
                    self.snacksPrice += 150
                    self.sandwichCnt += 1
                    self.sandwich = f"{self.sandwichCnt} * Sandwich (₹150)"
                case 3:
                    print("Added Cheese Popcorn (₹200)")
                    self.snacksPrice += 200
                    self.popcornCnt += 1
                    self.popcorn = f"{self.popcornCnt} * Cheese Popcorn (₹200)"
                case _:
                    print("Incorrect Input")
            self.snacks = int(input("Something More : "))

    def display(self):
        super().display()
        print("-----------------------------------------------")
        print("---------------------Snacks--------------------")
        print(self.coke)
        print(self.sandwich)
        print(self.popcorn)
        print("Price : ", self.snacksPrice)
