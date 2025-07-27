import random
class Person:
    seatCharges = 0
    people = 0
    def __init__(self):
        print("-----------------------------------------------")
        print("------------Enter Details of Person------------")
        self.personName = input("Enter Name : ")
        self.age = int(input("Enter Age : "))
        self.people = int(input("Enter Number of Seats : "))
        print("-----------------------------------------------")
        print("Seats : ")
        print("1. Recliner (₹200)\n2. Premium (₹250)\n3. Sofa(₹400)\n4. Normal(₹0)")
        self.seat = int(input("Enter the Type of Seat : "))
        match self.seat:
            case 1:
                self.seatType = "Recliner (₹200)"
                self.seatCharges += 200 * self.people
            case 2:
                self.seatType = "Premium (₹250)"
                self.seatCharges += 250 * self.people
            case 3:
                self.seatType = "Sofa (₹400)"
                self.seatCharges += 400 * self.people
            case 4:
                self.seatType = "Normal (₹0)"
                self.seatCharges += 0
            case _:
                print("Incorrect Input")

        print("-----------------------------------------------")

    def display(self):
        print("-----------------------------------------------")
        print("----------------Persons Details----------------")
        print("Booking Number : {}".format(random.randint(1000, 9999)))
        print("Name : {}".format(self.personName))
        print("Age : {}".format(self.age))
        print("Seat : {}".format(self.seatType))
        print("-----------------------------------------------")
