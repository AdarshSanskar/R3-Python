from Person import Person
class Movie(Person):
    movieName = ""
    movieTime = ""
    hallNumber = ""
    ticketPrice = 0.0
    def __init__(self):
        super().__init__()
        print("-----------------------------------------------")
        print("--------------Enter Movie Details--------------")
        print("Movies Available : ")
        print("1. Avengers - Doomsday")
        print("2. Captain America - Brave New World")
        print("3. Iron Heart")
        print("-----------------------------------------------")
        movie = int(input("Enter your Choice : "))
        match movie:
            case 1:
                print("-----------------------------------------------")
                self.movieName = "Avengers - Doomsday"
                print("Shows Timing : ")
                print("1. 5:00 PM - 8:30 PM (₹600)")
                print("2. 9:00 PM - 12:30 AM (₹600)")
                print("-----------------------------------------------")
                time = int(input("Enter your Choice : "))
                match(time):
                    case 1:
                        self.movieTime = "5:00 PM - 8:30 PM"
                    case 2:
                        self.movieTime = "9:00 PM - 12:30 AM"
                    case _:
                        print("Incorrect Input")
                self.hallNumber = "F1"
                self.ticketPrice = 600.0 * self.people
                print("-----------------------------------------------")
            case 2:
                print("-----------------------------------------------")
                self.movieName = "Captain America - Brave New World"
                print("Shows Timing : ")
                print("1. 4:00 PM - 7:30 PM (₹540)")
                print("2. 8:00 PM - 11:30 AM (₹540)")
                print("-----------------------------------------------")
                time = int(input("Enter your Choice : "))
                match (time):
                    case 1:
                        self.movieTime = "4:00 PM - 7:30 PM"
                    case 2:
                        self.movieTime = "8:00 PM - 11:30 AM"
                    case _:
                        print("Incorrect Input")
                self.hallNumber = "F2"
                self.ticketPrice = 540.0 * self.people
                print("-----------------------------------------------")
            case 3:
                print("-----------------------------------------------")
                self.movieName = "Iron Heart"
                print("Shows Timing : ")
                print("1. 3:00 PM - 6:30 PM (₹650)")
                print("2. 7:00 PM - 10:30 AM (₹650)")
                print("-----------------------------------------------")
                time = int(input("Enter your Choice : "))
                match (time):
                    case 1:
                        self.movieTime = "3:00 PM - 6:30 PM"
                    case 2:
                        self.movieTime = "7:00 PM - 10:30 AM"
                    case _:
                        print("Incorrect Input")
                self.hallNumber = "S1"
                self.ticketPrice = 650.0 * self.people
                print("-----------------------------------------------")

    def display(self):
        super().display()
        print("-----------------------------------------------")
        print("-----------------Movie Details-----------------")
        print("Movie Name : {}".format(self.movieName))
        print("Movie Time : {}".format(self.movieTime))
        print("Hall Number : {}".format(self.hallNumber))
        print("Number of People : {}".format(self.people))
        print("Ticket Price : {}".format(self.ticketPrice))
        print("-----------------------------------------------")