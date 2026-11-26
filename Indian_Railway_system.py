# Defining Variables for Indian Railway System

# train_name = "Rajdhani Express"
# train_number=12301
# ticket_price=2450.50
# is_ac_available=True 
# seat_numbers=[1,2,3,4,5]

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

# base_price = 1500
# service_charge = 100
# total_price = base_price + service_charge

# print(f"Base Price: ₹{base_price}")
# print(f"Service Charge: ₹{service_charge}")
# print(f"Total Price: ₹{total_price}")

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

# print("\n=== Booking Menu ===")
# choice = 0

# while choice !=3:
#     print("1. Book Tiket")
#     print("2. Check Status")
#     print("3. Exit")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#          print("Booking ticket ......")
#     elif choice == 2:
#       print("Checking Status")
#     elif choice ==3:
#         print("Thank you for using Indian Railways!")

#     else:
#         print("Invalid Choice!")


# Ticket price Calculator

# def calculate_ticket_price(distance,class_type):
#     base_rate = 0.5

#     if class_type == "Sleeper":
#         multiplier= 1.0
#     elif class_type =="AC 3 Tier":
#         multiplier= 1.5
#     elif class_type =="AC 2 Tier":
#         multiplier= 2.0
# #     elif class_type =="AC 1st class":
# #         multiplier = 3.0
# #     else:
# #         multiplier= 1.0
# #     price= distance * base_rate*multiplier

# #     return round(price,2)

# # distance =500
# # class_type= "AC 2 Tier"
# # price= calculate_ticket_price(distance,class_type)

# # print(f"Price for {distance}km in {class_type} :₹{price}")

# # Ticket Booking 

# def book_ticket(passenger_name,age,destination,class_type="Sleeper"):
#     ticket ={
#         "Passenger Name":passenger_name,
#         "Age": age,
#         "Destination":destination,
#         "Booking ID":f"BK{hash(passenger_name)%10000:04d}"
#     }
#     return ticket

# def get_passenger_details(*args,**kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:",kwargs)

# ticket1 = book_ticket("Rahul Kumar",28,"Mumbai")
# ticket2 = book_ticket("Priya Singh",32,"Delhi","AC 3 Tier")

# print("\nTicket 1:",ticket1)
# print("Ticket 2:",ticket2)

# get_passenger_details("Rahul",28,"Mumbai",class_type="Sleeper",meal_prefernce="Veg")

# calculate discount

# Calculate_discount = lambda price, discounted_percentage:price*(1 - discounted_percentage/100)

# original_price = 1500

# discounted_price =Calculate_discount(original_price,20)

# print(f"Original:₹{original_price}, Discounted Price:₹{discounted_price}")


# Trains details using build in functions  

# train =[
#     {"name":"Rajdhani","price":2500,"duration":16},
#     {"name":"Shatabdi","price":1800,"duration":8},
#     {"name":"Duronto","price":2000,"duration":12},
# ]

# # map

# train_names = list(map(lambda x :x['name'],train))
# print(f"\nTrain Names:{train_names}")

# # Filter  

# affordable_trains = list(filter(lambda x: x['price'] <2200,train))
# print("Affordable Trains :",[t["name"]for  t in affordable_trains])

# #Sorted 

# sorted_by_price = sorted(train,key=lambda x:x["price"])
# print("Sorted by price:", [t["name"] for t in sorted_by_price])


# oop based train system  

# class Train:
#     def __init__(self,train_number,name,source,destination,total_seats):
#         self.train_number=train_number
#         self.name=name
#         self.source=source
#         self.destination =destination
#         self.total_seats=total_seats
#         self.available_seats= total_seats

#     def display_info(self):
#         print(f"{self.train_number}-{self.name}")
#         print(f"Route:{self.source}to {self.destination}")
#         print(f"Available seats:{self.available_seats}/{self.total_seats}")

#     def book_seats(self):
#         if self.available_seats >0:
#             self.available_seats -=1
#             return True
#         return False

# train1= Train(12301,"Rajdhani Express", "Howrah","New Delhi",500)
# train2=Train(12001,"Shatabdi Express","Chennai","Banglore",400)

# print("===Train Information===")
# train1.display_info()
# print()
# train2.display_info()

# print("\n===Booking Tickets")

# if train1.book_seats():
#     print("Seat Booked sucessfully in Rajdhjani express !")
#     train1.display_info()


#Inheritance 

# class Train:
#     def __init__(self,train_number,name,source,destination):
#         self.train_number=train_number
#         self.name= name
#         self.source =source
#         self.destination = destination

#     def get_info(self):
#         return f"{self.train_number}-{self.name}"

# class ExpressTrain(Train):
#     def __init__(self, train_number, name, source, destination,max_speed):
#         super().__init__(train_number, name, source, destination)
#         self.max_speed=max_speed

#     def get_info(self):
#         base_info =super().get_info()
#         return f"{base_info}(Max Speed:{self.max_speed}km/h)"

# class PassengerTrain(Train):
#     def __init__(self, train_number, name, source, destination,stops):
#         super().__init__(train_number, name, source, destination)
#         self.stops= stops

#     def get_info(self):
#         base_info =super().get_info()
#         return f"{base_info} (Stops:{len(self.stops)})"

# express =ExpressTrain(12301,"Rajdhani Express", "Howrah","New Delhi",130)
# passenger= PassengerTrain(11001,"Intercity Express","Mumbai","Pune",["Lonavala","Khandala"])

# print("==Train Types")
# print(f"Express Train : {express.get_info()}")
# print(f"Passenger Train :{passenger.get_info()}")

# Encapsulation---Security of data  
# _ Protected attribute
# __private attribute  

# class BankAccount:
#     def __init__(self,account_number,initial_balance=0):
#         self._account_number=account_number
#         self.__balance =initial_balance

#     @property
#     def balance(self):
#         return self.__balance

#     @property
#     def account_number(self):
#         return self._account_number

#     def deposit(self,amount):
#         if amount >0:
#             self.__balance +=amount
#             print(f"Deposited Amount ₹{amount}. New Balance: ₹{self.__balance}")
#         else:
#             print("Invalid Amount!!!!")

#     def withdraw(self,amount):
#         if  0 < amount <=self.__balance:
#             self.__balance -=amount
#             print(f"Withdrawn Amount:  ₹{amount}. New Balance : ₹{self.__balance}")
#         else:
#             print("Invalid Withdrawal or Insufficent Funds!!!")

# class Ticket:

#     def __init__(self,passenger_name,train_number,seat_number ):
#         self.__passenger_name=passenger_name
#         self.__train_number=train_number
#         self.__seat_number =seat_number
#         self.__is_confirmed = False

#     def confirm_ticket(self):
#         self.__is_confirmed= True

#     def Details(self):
#         status = "Confirmed" if self.__is_confirmed else "Pending"
#         return {
#             "Passenger :" :self.__passenger_name,
#             "Train :" :self.__train_number ,
#             "Seat Number:" : self.__seat_number,
#             "Status:":status
#         }

# print("==Bank Account==")

# account = BankAccount("IR123456789")
# account.deposit(1000)
# account.withdraw(500)
# print("Current Balance:₹",account.balance)

# print("\n==Ticket==")

# ticket= Ticket("Veena Kutty",12301,"A5")
# print("Before Confirmation:",ticket.Details())
# ticket.confirm_ticket()
# print("After Confirmation:",ticket.Details())

#Polymorphism  

# class PaymentMethod:
#     def process_payment(Self,amount):
#         raise NotImplementedError("Sub-class must implement abstract method")

# class CreditCard(PaymentMethod):
#     def process_payment(Self, amount):
#         return f"Processing {amount} via Credit Card ."

# class Debitcard(PaymentMethod):
#     def process_payment(Self, amount):
#         return f"Processing {amount} via Debit Card ."
    
# class UPI(PaymentMethod):
#     def process_payment(Self, amount):
#         return f"Processing {amount} via UPI."

# class NetBanking(PaymentMethod):
#     def process_payment(Self, amount):
#         return f"Processing {amount} via NetBanking ."

# def make_payment(payment_method,amount):
#     return payment_method.process_payment(amount)

# print("==== Payment Method ====")

# payments = [
#     CreditCard(),
#     Debitcard(),
#     UPI(),
#     NetBanking()
# ]

# for payment in payments:
#     print(make_payment(payment,1500))


# Magic Method for customized Behvaiors  


# class Ticket:
#     def __init__(self,pnr,passenger_name):
#         self.pnr = pnr
#         self.passenger_name = passenger_name
#     def __str__(self):
#         return f"Ticket(PNR:{self.pnr}, Passenger : {self.passenger_name})"

#     def __repr__(self):
#         return f"Ticket(pnr='{self.pnr}', passenger_name ='{self.passenger_name}')"

#     def __eq__(self, other):
#         if isinstance(other,Ticket):
#             return self.pnr == other.pnr
#         return False

# print ("=== Ticket Magic Methods ===")

# ticket1 = Ticket("1234567890","Rahul Kumar")
# ticket2 = Ticket("1234567890","Rahul Kumar")
# ticket3 = Ticket("0987654321","Priya Singh")

# print(f"User-Friendly :{ticket1}")
# print(f"Developer -friendly :{repr(ticket2)}")
# print(f"Ticekt1 ==Ticekt2 :{ticket1==ticket2}")
# print(f"Ticekt1 ==Ticekt3 :{ticket1==ticket3}")


# Train Schedule Managment  

train_schedule=[]

train_schedule.append({
    "number": 12301,
    "name": "Rajdhani Express",
    "Departure": "14:00",
    "arrival":"10:30",
    "duration": "20h 30m "
})
        
train_schedule.append({
    "number": 12001,
    "name": "Shatabi Express",
    "Departure": "06:00",
    "arrival":"10:30",
    "duration": "4h 30m "
})  

# List operations

print("Train Schedules")
print(f"Total Trains :{len(train_schedule)}")

first_train =train_schedule[0]
print(f" First Train :{first_train}")

morining_trains =train_schedule[:1]
print(f"Morning Trains:{[t['name'] for t in morining_trains]}")

print(morining_trains)

