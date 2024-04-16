import sys  # Import the sys module for system-related operations
import random  # Import the random module for generating random numbers

# Define a Hotel class
class Hotel:
    # Initialize the Hotel object with optional parameters
    def __init__(self,
                 name=None,
                 age=None,
                 email=None,
                 contact_number=None,
                 room_types=None,
                 total_price=0,
                 choice=None,
                 occupant=None,
                 user=None,
                 bed_num=None,
                 floor=None,
                 per_item=1,
                 date=None
                 ):
        # Initializing instance variables
        self.date = date
        self.per_item = per_item
        self.floor = floor
        self.bed_num = bed_num
        self.user = user
        self.occupant = occupant
        self.choice = choice
        self.name = name
        self.age = age
        self.email = email
        self.contact_number = contact_number
        self.room_types = room_types
        self.total_price = total_price
        # Define room types with default values
        self.room_types = [
            {
                "Room Type": "Standard",
                "Occupancy Capacity": 5,
                "Pricing": 100
            },
            {
                "Room Type": "Deluxe",
                "Occupancy Capacity": 6,
                "Pricing": 150
            },
            {
                "Room Type": "Executive Suite",
                "Occupancy Capacity": 8,
                "Pricing": 250
            },
            {
                "Room Type": "Family Suite",
                "Occupancy Capacity": 10,
                "Pricing": 350
            }
        ]

    # Display main menu options
    def main_menu(self):
        print()  # Print a blank line for readability
        print("Welcome to Compsci Hotel")  # Display the hotel name
        print("1.View Available Rooms")  # Option to view available rooms
        print("2.Book a room")  # Option to book a room
        print("3.Edit/Cancel Booking")  # Option to edit or cancel booking
        print("4.Display User Info")  # Option to display user info
        print("5.Exit")  # Option to exit the program
        user = input("Enter your Choice:1-4:")  # Get user input for menu choice
        if user == '1':
            self.view_rooms()  # Call the view_rooms method if user chooses option 1
        elif user == '2':
            self.book_room()  # Call the book_room method if user chooses option 2
        elif user == '3':
            self.edit_booking()  # Call the edit_booking method if user chooses option 3
        elif user == '4':
            self.print_userDetails()  # Call the print_userDetails method if user chooses option 4
            print()  # Print a blank line for readability
            self.main_menu()  # Return to the main menu
        elif user == '5':
            print("The program will now exit!")  # Inform the user that the program will exit
            sys.exit()  # Exit the program using sys.exit()
        else:
            print("Invalid Choice. Try Again!")  # Inform the user of an invalid choice
            self.main_menu()  # Return to the main menu

    # View available rooms
    def view_rooms(self):
        print("Available Rooms:")  # Display available rooms header
        self.print_rooms()  # Call the print_rooms method to display room details
        self.main_menu()  # Return to the main menu

    # Print room details
    def print_rooms(self):
        n = 1  # Initialize a counter for room numbers
        print()  # Print a blank line for readability
        for room in self.room_types:  # Iterate through each room type
            print(f"Room Number {n}")  # Print the room number
            print(f"Room Type:{room['Room Type']}")  # Print the room type
            print(f"Occupancy Limit:{room['Occupancy Capacity']}")  # Print the occupancy limit
            print(f"Price:${room['Pricing']}")  # Print the price
            n += 1  # Increment the room number
            print()  # Print a blank line for readability

    # Book a room
    def book_room(self):
        if self.total_price > 0:
            q = input("You have previous Booking. Do you want to delete your previous booking?(y-n)")
            if q == 'y':
                self.edit_booking()
                print("Previous Booking was Deleted!")
            else:
                self.main_menu()
        print("Enter your Personal Information:")
        self.name = input("Enter your name:")
        self.age = input("Enter your Age:")
        self.email = input("Enter your Email:")
        self.contact_number = input("Enter your Contact Number:")
        self.date = input("Enter the date of your reservation:")
        self.print_rooms()
        while True:
            self.user = int(input("Enter your room choice:1-4:"))
            if self.user == 1:
                self.choice = self.room_types[self.user - 1]
                self.capacity()
                break
            elif self.user == 2:
                self.choice = self.room_types[self.user - 1]
                self.capacity()
                break
            elif self.user == 3:
                self.choice = self.room_types[self.user - 1]
                self.capacity()
                break
            elif self.user == 4:
                self.choice = self.room_types[self.user - 1]
                self.capacity()
                break
            else:
                print("Invalid Choice! Try Again.")
        self.total_price += self.choice['Pricing']
        print("Chosen Room Type:")
        self.print_chosen_room()
        print("Ads On:")
        ask = input("Do you want to add beds?(y-n):")
        if ask == 'y':
            self.bed_num = int(input("How many beds do you want in the room?"))
            self.total_price = self.total_price + (self.bed_num * 20)
        ask1 = input("Do you want to be on Higher Floor View?(y-n):")
        if ask1 == 'y':
            floor = random.randint(5, 10)
            self.floor = floor
            self.total_price += 30
        ask2 = input("Do you want to add personal hygiene items?(y-n):")
        if ask2 == 'y':
            self.total_price += 10
            self.per_item = 1
        else:
            self.per_item = 0
        print()
        self.print_userDetails()
        print()
        self.main_menu()

    # Print user details
    def print_userDetails(self):
        if self.total_price == 0:
            print("There is no information about the user")
            self.main_menu()
        else:
            print()
            print("User Booked Information:")
            print(f"Name:{self.name}")
            print(f"Age:{self.age}")
            print(f"Email:{self.email}")
            print(f"Contact Number:{self.contact_number}")
            print(f"Reservation Date:{self.date}")
            print(f"Occupants:{self.occupant}")
            print(f"Floor Level:{self.floor}")
            if self.per_item == 1:
                print("Personal Hygiene items: Subscribed")
            else:
                print("Personal Hygiene items: Not Subscribed")
            print("Chosen Room")
            self.print_chosen_room()
            print(f"Total Price:${self.total_price}")

    # Check room capacity
    def capacity(self):
        while True:
            self.occupant = int(input("Enter how many occupants:"))
            if self.room_types[self.user - 1]['Occupancy Capacity'] < self.occupant:
                print("The occupant number is greater than the capacity of the room! Please try again!")
            else:
                break

    # Edit or cancel booking
    def edit_booking(self):
        print()
        print("1.Edit Reservation Date")
        print("2.Cancel the Reservation")
        print("3.Back to Menu")
        ask = input("Enter your choice(1-3):")
        if ask == '1':
            self.date = input("Enter new Date of reservation:")
            self.main_menu()
        elif ask == '2':
            print("Your Whole payment will be refunded into half of your payment.")
            ask1 = input("Are you sure do you want to cancel?(y-n):")
            if ask1 == 'y':
                self.name = None
                self.age = None
                self.email = None
                self.contact_number = None
                self.date = None
                self.total_price = 0
                self.per_item = 0
                self.floor = None
                self.bed_num = 0
                self.occupant = 0
                self.user = None
                self.choice = None
                print("User Reservation Deleted")
            else:
                print("Deleting Booking Cancelled!")
                self.main_menu()
        elif ask == '3':
            self.main_menu()
        else:
            print("Invalid Input! try again!")
            self.edit_booking()
        self.main_menu()

    # Print chosen room details
    def print_chosen_room(self):
        print(f"Room Type:{self.choice['Room Type']}")
        print(f"Occupancy Limit:{self.choice['Occupancy Capacity']}")
        print(f"Price:${self.choice['Pricing']}")

# Create an instance of the Hotel class
start = Hotel()
# Call the main_menu method to start the program
start.main_menu()
