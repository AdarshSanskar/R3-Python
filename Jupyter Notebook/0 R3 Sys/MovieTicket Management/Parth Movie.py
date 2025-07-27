# import random
# import os
#
# ADMIN_PASSWORD = "parth123"
# movies = {
#     1: {"name": "Animal", "price": 150, "seats": 50},
#     2: {"name": "Kabir Singh", "price": 200, "seats": 40},
#     3: {"name": "Murder", "price": 250, "seats": 20},
#     4: {"name": "Fifty Shades of grey", "price": 300, "seats": 100}
# }
# bookings = []
#
# class Person:
#     def _init_(self, name):
#         self.name = name
#
# class User(Person):
#     def _init_(self, name):
#         super()._init_(name)
#
#     def book_ticket(self):
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print("\n🎞 Available Movies:")
#         for id, m in movies.items():
#             print(f"{id}. {m['name']} - ₹{m['price']} | Seats Left: {m['seats']}")
#
#         try:
#             movie_id = int(input("\nEnter movie ID: "))
#             movie = movies[movie_id]
#             count = int(input("How many tickets?: "))
#             if count > movie['seats']:
#                 print(f"❌ Only {movie['seats']} seats available.")
#                 return
#             total = movie['price'] * count
#             booking_id = random.randint(1000, 9999)
#             movie["seats"] -= count
#             bookings.append({"user": self.name,"movie": movie["name"],"tickets": count,"total": total,"id": booking_id})
#             #Ticket Generation
#             print("\n✅ Booking Confirmed!")
#             print(" ----- Ticket -----")
#             print(f"Booking ID : {booking_id}")
#             print(f"Name       : {self.name}")
#             print(f"Movie      : {movie['name']}")
#             print(f"Tickets    : {count}")
#             print(f"Total Cost : ₹{total}")
#             print("Enjoy your movie! 🎬")
#         except Exception as e:
#             print("❌ Something Wrong Input:", e)
#
#     def view_bookings(self):
#         print(f"\n Your Bookings ({self.name}):")
#         for b in bookings:
#             if b['user'] == self.name:
#                 print(f"ID: {b['id']} | Movie: {b['movie']} | Tickets: {b['tickets']} | ₹{b['total']}")
#
# class Admin(Person):
#     def _init_(self, name):
#         super()._init_(name)
#
#     def view_all_bookings(self):
#         print("\nAll Bookings:")
#         for b in bookings:
#             print(f"User: {b['user']} | Movie: {b['movie']} | Tickets: {b['tickets']} | ₹{b['total']}")
# def main():
#     while True:
#         print("\n🎬 Movie Booking System")
#         print("1. User Login")
#         print("2. Admin Login")
#         print("3. Exit")
#         choice = input("Choose option: ")
#         if choice == '1':
#             name = input("Enter your name: ")
#             user = User(name)
#             user_menu(user)
#         elif choice == '2':
#             name = input("Enter admin name: ")
#             password = input("Enter admin password: ")
#             if password == ADMIN_PASSWORD:
#                 admin = Admin(name)
#                 admin.view_all_bookings()
#             else:
#                 print("❌ Incorrect password!")
#         elif choice == '3':
#             print("Thank You for using the Movie Booking System!")
#             break
#         else:
#             print("❌ Invalid choice.")
#
# def user_menu(user):
#     while True:
#         print(f"\n👤 Welcome {user.name}")
#         print("1. Book Ticket")
#         print("2. View My Bookings")
#         print("3. Logout")
#         choice = input("Choose option: ")
#
#         if choice == '1':
#             user.book_ticket()2
#         elif choice == '2':
#             user.view_bookings()
#         elif choice == '3':
#             break
#         else:
#             print("❌ Invalid choice.")
#
#
# if _name_ == "_main_":
#     main()

import random
import os

ADMIN_PASSWORD = "parth123"
movies = {
    1: {"name": "Animal", "price": 150, "seats": 50},
    2: {"name": "Kabir Singh", "price": 200, "seats": 40},
    3: {"name": "Murder", "price": 250, "seats": 20},
    4: {"name": "Fifty Shades of grey", "price": 300, "seats": 100}
}
bookings = []


class Person:
    def __init__(self, name):
        self.name = name


class User(Person):
    def __init__(self, name):
        super().__init__(name)

    def book_ticket(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n🎞 Available Movies:")
        for id, m in movies.items():
            print(f"{id}. {m['name']} - ₹{m['price']} | Seats Left: {m['seats']}")

        try:
            movie_id = int(input("\nEnter movie ID: "))
            if movie_id not in movies:
                print("❌ Invalid movie ID.")
                return

            movie = movies[movie_id]
            count = int(input("How many tickets?: "))

            if count <= 0:
                print("❌ Number of tickets must be positive.")
                return

            if count > movie['seats']:
                print(f"❌ Only {movie['seats']} seats available.")
                return

            total = movie['price'] * count

            # Generate unique booking ID
            booking_id = self._generate_unique_booking_id()

            movie["seats"] -= count
            bookings.append({
                "user": self.name,
                "movie": movie["name"],
                "tickets": count,
                "total": total,
                "id": booking_id
            })

            # Ticket Generation
            print("\n✅ Booking Confirmed!")
            print(" ----- Ticket -----")
            print(f"Booking ID : {booking_id}")
            print(f"Name       : {self.name}")
            print(f"Movie      : {movie['name']}")
            print(f"Tickets    : {count}")
            print(f"Total Cost : ₹{total}")
            print("Enjoy your movie! 🎬")

        except ValueError:
            print("❌ Please enter valid numbers.")
        except Exception as e:
            print("❌ Something went wrong:", e)

    def _generate_unique_booking_id(self):
        """Generate a unique booking ID"""
        while True:
            booking_id = random.randint(1000, 9999)
            if not any(b['id'] == booking_id for b in bookings):
                return booking_id

    def view_bookings(self):
        print(f"\n📋 Your Bookings ({self.name}):")
        user_bookings = [b for b in bookings if b['user'] == self.name]

        if not user_bookings:
            print("No bookings found.")
            return

        for b in user_bookings:
            print(f"ID: {b['id']} | Movie: {b['movie']} | Tickets: {b['tickets']} | ₹{b['total']}")

    def cancel_booking(self):
        """Cancel a booking and restore seats"""
        user_bookings = [b for b in bookings if b['user'] == self.name]

        if not user_bookings:
            print("❌ No bookings to cancel.")
            return

        print(f"\n📋 Your Bookings ({self.name}):")
        for b in user_bookings:
            print(f"ID: {b['id']} | Movie: {b['movie']} | Tickets: {b['tickets']} | ₹{b['total']}")

        try:
            booking_id = int(input("\nEnter booking ID to cancel: "))

            for i, booking in enumerate(bookings):
                if booking['id'] == booking_id and booking['user'] == self.name:
                    # Restore seats
                    for movie_id, movie in movies.items():
                        if movie['name'] == booking['movie']:
                            movie['seats'] += booking['tickets']
                            break

                    # Remove booking
                    bookings.pop(i)
                    print("✅ Booking cancelled successfully!")
                    return

            print("❌ Booking not found.")

        except ValueError:
            print("❌ Please enter a valid booking ID.")


class Admin(Person):
    def __init__(self, name):
        super().__init__(name)

    def view_all_bookings(self):
        print("\n📊 All Bookings:")
        if not bookings:
            print("No bookings found.")
            return

        for b in bookings:
            print(f"User: {b['user']} | Movie: {b['movie']} | Tickets: {b['tickets']} | ₹{b['total']} | ID: {b['id']}")

    def view_movie_stats(self):
        """View movie statistics"""
        print("\n📈 Movie Statistics:")
        for movie_id, movie in movies.items():
            total_seats = movie['seats']
            movie_bookings = [b for b in bookings if b['movie'] == movie['name']]
            booked_tickets = sum(b['tickets'] for b in movie_bookings)
            revenue = sum(b['total'] for b in movie_bookings)

            print(f"{movie['name']}:")
            print(f"  Available Seats: {total_seats}")
            print(f"  Booked Tickets: {booked_tickets}")
            print(f"  Total Revenue: ₹{revenue}")
            print()


def main():
    while True:
        print("\n🎬 Movie Booking System")
        print("1. User Login")
        print("2. Admin Login")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == '1':
            name = input("Enter your name: ").strip()
            if not name:
                print("❌ Name cannot be empty.")
                continue
            user = User(name)
            user_menu(user)

        elif choice == '2':
            name = input("Enter admin name: ").strip()
            password = input("Enter admin password: ")
            if password == ADMIN_PASSWORD:
                admin = Admin(name)
                admin_menu(admin)
            else:
                print("❌ Incorrect password!")

        elif choice == '3':
            print("Thank You for using the Movie Booking System!")
            break
        else:
            print("❌ Invalid choice.")


def user_menu(user):
    while True:
        print(f"\n👤 Welcome {user.name}")
        print("1. Book Ticket")
        print("2. View My Bookings")
        print("3. Cancel Booking")
        print("4. Logout")
        choice = input("Choose option: ")

        if choice == '1':
            user.book_ticket()
        elif choice == '2':
            user.view_bookings()
        elif choice == '3':
            user.cancel_booking()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice.")


def admin_menu(admin):
    while True:
        print(f"\n👑 Admin Panel - {admin.name}")
        print("1. View All Bookings")
        print("2. View Movie Statistics")
        print("3. Logout")
        choice = input("Choose option: ")

        if choice == '1':
            admin.view_all_bookings()
        elif choice == '2':
            admin.view_movie_stats()
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice.")
main()