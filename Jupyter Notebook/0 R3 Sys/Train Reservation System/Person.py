class Person:
    def __init__(self):
        self.name = input("Enter Passenger Name: ")
        self.age = int(input("Enter Age: "))
        self.gender = input("Enter Gender: ")

    def get_details(self):
        print("Passenger Name :", self.name)
        print("Age            :", self.age)
        print("Gender         :", self.gender)
