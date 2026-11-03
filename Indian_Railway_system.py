# Defining Variables for Indian Railway System

train_name = "Rajdhani Express"
train_number=12301
ticket_price=2450.50
is_ac_available=True 
seat_numbers=[1,2,3,4,5]

# Showing details  using print Function 

# print("Train  Name:",train_name)
# print("Train Number:",train_number)
# print("Ticket Price:",ticket_price)
#print("AC Availability:",is_ac_available)
# print("Seat Number:",seat_numbers)

# Show the data types of the variables using type functions

# print("The data type of the train_name:",type(train_name))
# print("The data type of the train_number:",type(train_number))
# print("The data type of the ticekt_price:",type(ticket_price))
# print("The data type of the is_ac_available:",type(is_ac_available))
# print("The data type of the seat_numbers:",type(seat_numbers))

# Getting passenger information 
# print("=== Indian Railway Booking System ===")
# passenger_name = input("Enter Passenger name:")
# age = int(input("Enter Age:"))
# destination = input("Enter Destination:")

# Display booking confirmation

# print("\n=== Booking details ===")
# print(f"passenger:{passenger_name}")
# print(f"Age:{age}")
# print(f"destination:{destination}")
# print("Booking confirmed")

#Arithimetic Operators 

base_price = 1500
service_charge = 100
total_price = base_price + service_charge

print(f"Base Price: ₹{base_price}")
print(f"Service Charge: ₹{service_charge}")
print(f"Total Price: ₹{total_price}")

# Comparison Operators
# passenger_age = 25
# senior_citizen_age = 60
# is_senior =passenger_age >= senior_citizen_age

# print(f"\nIs passenger senior citizen?{is_senior}") 

# Logical Operators

# has_ticket =True
# has_id_proof = True
# can_board = has_ticket and  has_id_proof

# print(f"Can Board Train? {can_board}")

# Control Flow -If statements
# Age bases Pricing

# Age = int(input("Enter passenger age: "))

# if Age < 5: 
#     price = 0
#     category = "Infant(Free)"
# elif Age < 12 :
#     price = 750
#     category = "Child (50% Discount)"
# elif Age >=60:
#     price = 1200
#     category = "Senior Citizen(20% Discount)"
# else:
#     price = 1500
#     category = "Adult"

# print(f"Category:{category}")
# print(f"Ticket Price: ₹{price}")

# For Loop - Display available Trains

# trains = [
#     {"name":"Rajdhani Express",
#      "number":12301,
#      "destination":"New Delhi"},
#      {"name":"Shatabi Express",
#      "number":12001,
#     "destination":"Chennai"},
#     {"name":"Duranto Express",
#     "number":12291,
#     "destination":"Mumbai"}
# ]

# print("Available Trains: ")
# for train in trains :
#     print(f"{train['number']} - {train['name']} to {train['destination']}")


# While Loop -Booking System Menu 

print("\n=== Booking Menu ===")
choice = 0

while choice !=3:
    print("1. Book Tiket")
    print("2. Check Status")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
         print("Booking ticket ......")
    elif choice == 2:
      print("Checking Status")
    elif choice ==3:
        print("Thank you for using Indian Railways!")

    else:
        print("Invalid Choice!")


