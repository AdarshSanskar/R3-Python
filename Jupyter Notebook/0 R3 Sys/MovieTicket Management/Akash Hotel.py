# import os
# import random
#
# # Base class
# class Person:
#     def _init_(self, name, mobile):
#         self.name = name
#         self.mobile = mobile
#
#     def display_customer(self):
#         print(f"\nCustomer Name  : {self.name}")
#         print(f"Mobile Number  : {self.mobile}")
#
# # Derived class
# class Order(Person):
#     menu = {
#         "Starter": {
#             1: ['Papad', 20],
#             2: ['Masala-papad', 40],
#             3: ['Nagli-papad', 50]
#         },
#         "Veg": {
#             1: ['Shevbhajii', 120],
#             2: ['Shevbhajitadka', 180],
#             3: ['Paneer', 140],
#             4: ['Paneer masala', 180],
#             5: ['Paneer tikka masala', 200],
#             6: ['Vegkolhapuri', 250],
#             7: ['Mix-veg', 170],
#             8: ['Kaju-masala', 230],
#             9: ['Veg-pulav', 160],
#             10: ['Chana masala', 190]
#         },
#         "Non-Veg": {
#             1: ['Chicken thali', 250],
#             2: ['Mutton thali', 350],
#             3: ['Egg-curry', 120],
#             4: ['Chicken masala', 200],
#             5: ['Mutton masala', 400],
#             6: ['Butter chicken', 250],
#             7: ['Chicken tikka', 300],
#             8: ['Chicken-biryani', 250],
#             9: ['Mutton-fry', 450],
#             10: ['Chicken-soup', 60]
#         },
#         "Drinks": {
#             1: ['Water', 50],
#             2: ['Tak', 40],
#             3: ['Masala-tak', 50],
#             4: ['Cold-drinks', 100],
#             5: ['Lassi', 60]
#         },
#         "Rice": {
#             1: ['Plain-rice', 100],
#             2: ['Jira-rice', 150],
#             3: ['Dal-khechada', 180]
#         }
#     }
#
#     def _init_(self, name, mobile):
#         super()._init_(name, mobile)
#         self.order_list = []
#
#     def show_menu(self, category):
#         items = self.menu[category]
#         print(f"\n📋 {category.upper()} MENU")
#         print("-" * 30)
#         for idx, (item, price) in items.items():
#             print(f"{idx}. {item} - ₹{price}")
#         print("-" * 30)
#
#     def take_order(self):
#         cat_map = {
#             1: "Starter",
#             2: "Veg",
#             3: "Non-Veg",
#             4: "Drinks",
#             5: "Rice"
#         }
#         while True:
#             print("\nChoose a Menu Category:")
#             print("1. Starter Menu")
#             print("2. Veg Menu")
#             print("3. Non-Veg Menu")
#             print("4. Drinks Menu")
#             print("5. Rice Menu")
#             print("0. Finish Ordering")
#
#             try:
#                 choice = int(input("Enter choice: "))
#             except ValueError:
#                 print("Please enter a valid number.")
#                 continue
#
#             if choice == 0:
#                 break
#
#             category = cat_map.get(choice)
#             if not category:
#                 print("Invalid category!")
#                 continue
#
#             self.show_menu(category)
#
#             try:
#                 item_no = int(input("Enter item number to order: "))
#                 qty = int(input("Enter quantity: "))
#             except ValueError:
#                 print("Invalid input—numbers only.")
#                 continue
#
#             if item_no in self.menu[category]:
#                 item, price = self.menu[category][item_no]
#                 self.order_list.append((item, price, qty))
#                 print("Item added!\n")
#             else:
#                 print("Invalid item number!")
#
#     def generate_bill(self):
#         os.system('cls' if os.name == 'nt' else 'clear')
#         self.display_customer()
#         print("\n🧾 BILL")
#         print("-" * 40)
#         total = 0
#         for item, price, qty in self.order_list:
#             amount = price * qty
#             print(f"{item:20} x{qty:<3} ₹{price:<4} = ₹{amount}")
#             total += amount
#
#         bill_no = random.randint(1000, 9999)
#         print("-" * 40)
#         print(f"Total Amount   : ₹{total}")
#         print(f"Bill Number    : #{bill_no}")
#         print("-" * 40)
#
# def main():
#     print("🏨 Welcome to Hotel Bhagyshree!")
#     name = input("Enter your name: ")
#     mobile = input("Enter your mobile number: ")
#     customer = Order(name, mobile)
#     customer.take_order()
#     customer.generate_bill()
#
# if _name_ == "_main_":
#     main()

import os
import random

# Base class
class Person:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile

    def display_customer(self):
        print(f"\nCustomer Name  : {self.name}")
        print(f"Mobile Number  : {self.mobile}")

# Derived class
class Order(Person):
    menu = {
        "Starter": {
            1: ['Papad', 20],
            2: ['Masala-papad', 40],
            3: ['Nagli-papad', 50]
        },
        "Veg": {
            1: ['Shevbhajii', 120],
            2: ['Shevbhajitadka', 180],
            3: ['Paneer', 140],
            4: ['Paneer masala', 180],
            5: ['Paneer tikka masala', 200],
            6: ['Vegkolhapuri', 250],
            7: ['Mix-veg', 170],
            8: ['Kaju-masala', 230],
            9: ['Veg-pulav', 160],
            10: ['Chana masala', 190]
        },
        "Non-Veg": {
            1: ['Chicken thali', 250],
            2: ['Mutton thali', 350],
            3: ['Egg-curry', 120],
            4: ['Chicken masala', 200],
            5: ['Mutton masala', 400],
            6: ['Butter chicken', 250],
            7: ['Chicken tikka', 300],
            8: ['Chicken-biryani', 250],
            9: ['Mutton-fry', 450],
            10: ['Chicken-soup', 60]
        },
        "Drinks": {
            1: ['Water', 50],
            2: ['Tak', 40],
            3: ['Masala-tak', 50],
            4: ['Cold-drinks', 100],
            5: ['Lassi', 60]
        },
        "Rice": {
            1: ['Plain-rice', 100],
            2: ['Jira-rice', 150],
            3: ['Dal-khechada', 180]
        }
    }

    def __init__(self, name, mobile):
        super().__init__(name, mobile)
        self.order_list = []

    def show_menu(self, category):
        items = self.menu[category]
        print(f"\n📋 {category.upper()} MENU")
        print("-" * 30)
        for idx, (item, price) in items.items():
            print(f"{idx}. {item} - ₹{price}")
        print("-" * 30)

    def take_order(self):
        cat_map = {
            1: "Starter",
            2: "Veg",
            3: "Non-Veg",
            4: "Drinks",
            5: "Rice"
        }
        while True:
            print("\nChoose a Menu Category:")
            print("1. Starter Menu")
            print("2. Veg Menu")
            print("3. Non-Veg Menu")
            print("4. Drinks Menu")
            print("5. Rice Menu")
            print("0. Finish Ordering")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 0:
                break

            category = cat_map.get(choice)
            if not category:
                print("Invalid category!")
                continue

            self.show_menu(category)

            try:
                item_no = int(input("Enter item number to order: "))
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input—numbers only.")
                continue

            if item_no in self.menu[category]:
                item, price = self.menu[category][item_no]
                self.order_list.append((item, price, qty))
                print("Item added!\n")
            else:
                print("Invalid item number!")

    def generate_bill(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.display_customer()
        print("\n🧾 BILL")
        print("-" * 40)
        total = 0
        for item, price, qty in self.order_list:
            amount = price * qty
            print(f"{item:20} x{qty:<3} ₹{price:<4} = ₹{amount}")
            total += amount

        bill_no = random.randint(1000, 9999)
        print("-" * 40)
        print(f"Total Amount   : ₹{total}")
        print(f"Bill Number    : #{bill_no}")
        print("-" * 40)

def main():
    print("🏨 Welcome to Hotel Bhagyshree!")
    name = input("Enter your name: ")
    mobile = input("Enter your mobile number: ")
    customer = Order(name, mobile)
    customer.take_order()
    customer.generate_bill()

main()