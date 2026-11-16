
# # For LOOP

# # for i in range(0,11):
# #     print(i)

# # for i in range(0,21):
# #     if i %2==0:
# #         print(i)

# # for i in range(0,21):
# #     if i %2!=0:
# #         print(i) 

# # num =5 

# # for i in range(1,11):
# #     print(num, "x", i, "=", num*i)

# # total =0

# # for i in range(1,11):
# #     total = total + 1

# # print("Total:", total)

# # num = 5
# # fact = 1

# # for i in  range(1, num + 1):
# #     fact = fact* i

# # print("Factorial:", fact)


# # chars= "Python"

# # for char in chars:
# #     print(char)

# # names = ["Aarti","Suraj","Tejas","OM","Yash","Yash"]

# # for name in names:
# #     print(name)


# # num =[10,30,20,45,200,60,202,756]

# # largest = num[0]

# # for i in num:
# #     if i > largest:
# #         largest=i
# # print("The Largest number:", largest)

# # text = "python programming"
# # count = 0

# # for char in text:
# #     if char in "aeiou":
# #         count +=1

# # print("Number of Vowels:", count)

# #While LOOP

# # i = 1

# while i <=10:
#     print(i)
#     i+=1

# i = 1

# total = 0

# while i <=10:
#     total += i
#     i+=1

# print("Total :" ,total)

# num  = 12345
# reverse = 0

# while num >0 :
#     digit = num % 10
#     reverse = reverse * 10 + digit 
#     num //= 10
# print("Reverse number:",reverse)


# num = 123456

# count = 0

# while num >  0:
#     num //= 10
#     count += 1

# # print("The number of digits:", count)

# # correct_number = 4

# # guess = int(input("Enter a number:"))

# # while guess != correct_number:
# #     print("Wrong Number!!")

# #     guess = int(input("Enter a number" ))

# # print("Correct Guess!!")


# # Loop Control statements

# # for i in range(20):
# #     if i ==12:
# #         break
# #     print(i)

# # to skip any value  
# for i in range(20):
#     if i ==12:
#         continue
#     print(i)

# # Defining variale for indian railway system  
# train_name= "Rajdhani Express"
# train_number = 12301
# ticket_price = 2450.50
# is_ac_available =True
# seat_numbers = [1,2,3,4,5]

# print("Train Name :" ,train_name)
# print("Train Number :", train_number)
# print("Train Price :", ticket_price)
# print("AC Availability :", is_ac_available)
# print("Seat numbers :", seat_numbers)




# print("The data type of train_name:", type(train_name))
# print("The data type of train_number:", type(train_number))
# print("The data type of ticket_price:", type(ticket_price))
# print("The data type of is_ac_available:", type(is_ac_available))
# print("The data type of seat_numbers:", type(seat_numbers))


# print(" === Indian Railway Booking System ===")
# passenger_name=input("Enter passenger Name :")
# age = int(input("Enter Age:"))
# destination= input("Enter Destination:")

# print("\n=== Booking details ===")
# print(f"passenger:{passenger_name}")
# print(f"age:{age}")
# print(f"destination:{destination}")
# print("Booking Confirmed")

# base_price = 1500
# service_charge =100
# total_price= base_price + service_charge

# print(f"Base price: ₹{base_price}")
# print(f"Service Charge : ₹{service_charge}")
# print(f"Total Price : ₹{total_price}")

# passenger_age=25
# senior_citizen_age = 60
# is_senior = passenger_age>= senior_citizen_age

# print(f"\nIs passenger senior citizen? {is_senior}")

# has_ticket =True
# has_id_proof =True
# can_board= has_ticket and  has_id_proof

# print(f"can board Train?{can_board}")


# age = int(input("Enter Passenger age :"))

# if age < 5:
#     price = 0
#     category= "Infant (Free)"
# elif age < 12: 
#     price = 750
#     category = "child (50 % Discount)"
# elif age >= 60:
#     price = 1200
#     category=" Senior Citizen {20% Discount }"
# else:
#     price = 1500
#     category = "adult"

# print(f"Category:{category}")
# print(f"Ticke Price:{price}")


# trains =[
#     {"name":"Rajdhani Express",
#      "number": 12301,
#      "destination":"New Delhi"},
#     {"name":"Shatabi Expres",
#     "number": 12001,
#     "destination":"Chennai"} ,
#      {"name":"Duronto Express",
#     "number": 12291,
#     "destination":"Mumbai"}
# ]

# print("Available Trains: ")
# for train in trains :
#     print(f"{train['number']} - {train['name']} to {train['destination']}")




# def greet():
#     print("Hello Mister/Miss!!")
# greet()

# def greet():
#     name=input("Enter your name!:")
#     print(f"Hello! {name} !How are you?")
# greet()

# def greet(name):
#     print(f"Hello! {name}! How are you?")
# # greet("Venna")

# def greet(name="Guest"):
#     print(f"Hello!{name}! How are you?")
# greet("Aarti")


# def welcome():
#     print("Welcome to the professional Course!!")
#     print("Lets Learn Data Science !!")

# welcome()

# def age_verification():
#     age = int(input("Enter you age:  "))

#     if age >=18:
#         print("Applicable for the License !!")
#     else:
#         print("Try again Next Time")

# age_verification()


# def login(user_name):
#     password=input("Enter your Password:")
#     while password!= "Aarti0000":
#         print("Wrong Password")
#         password= input("Enter your Password: ")
        
#     else:
#         print(f"Hello!{user_name}")
# login("Aarti")

# def add(a,b):
#     return a+b

# def multiply(x,y):
#     print(x*y)

# add(2,3)
# multiply(2,3)

# print("ADD: ", add(2,3))
# print("Multiply :",multiply(2,3))

# def student(name,age):
#     print(f"{name} is {age} years old!")

# student(age=27,name="Aarti")


# def total_score(*marks):
#     print("Marks :",marks)
#     print("Total Score:", sum(marks))
#     import  numpy as np
#     print("Percentage :", np.mean(marks))
# total_score(85,97,99)


# def employee_details(**details):
#     for key, value in details.items():
#         print(key,":", value)

# employee_details(
#     Emp_name = "Aarti",
#     Age= 27,
#     Department= "IT",
#     Salary="10k"

# )


# # List 

# states = ["Maharashtra","Kerala","Punjab","Tamil Nadu","Gujarat"]

# print("Original List:",states)

# # Add Elements 
# states.append("Karnataka")
# states.insert(2,"Rajasthan")        #insert at index 
# print("After Append & Insert :", states)


# #Extend With another list 

# states.extend(["Goa","Bihar"])
# print("After Extend :",states)

# # Remove elements

# states.remove("Punjab")   # remove Specifuc element 
# popped = states.pop()           #remove last element 
# print("Removed Element:", popped)
# print("After Remove & Pop:",states)

# # sorting & reversing

# states.sort()
# print("Sorted List:",states)
# states.reverse()
# print("Reversed List:",states)

# # index & count

# print("Index of Kerala :",states.index("Kerala"))
# print("Count of Kerala :",states.count("Kerala"))


# # Copy & Clear  

# copy_states=states.copy()
# print("Copied List:",copy_states)
# states.clear()
# print("Cleared List:",states)


# TUPLE 
cities =("Mumbai","Delhi","Bengaluru","Chennai","Kolkata","Mumbai")

print("Tuple:", cities)

# count
print("Count  of Mumbai:",cities.count("Mumbai"))

#Index
print("Index of Chennai:", cities.index("Chennai"))


# Length 
print("Length :", len(cities))

#Mmebership
print("Delhi in Tuple?:","Delhi" in cities)

# min and max (alphabetical )
print("Min :",min(cities))
print("Max :",max(cities))