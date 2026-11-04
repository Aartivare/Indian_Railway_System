
# For LOOP

# for i in range(0,11):
#     print(i)

# for i in range(0,21):
#     if i %2==0:
#         print(i)

# for i in range(0,21):
#     if i %2!=0:
#         print(i) 

# num =5 

# for i in range(1,11):
#     print(num, "x", i, "=", num*i)

# total =0

# for i in range(1,11):
#     total = total + 1

# print("Total:", total)

# num = 5
# fact = 1

# for i in  range(1, num + 1):
#     fact = fact* i

# print("Factorial:", fact)


# chars= "Python"

# for char in chars:
#     print(char)

# names = ["Aarti","Suraj","Tejas","OM","Yash","Yash"]

# for name in names:
#     print(name)


# num =[10,30,20,45,200,60,202,756]

# largest = num[0]

# for i in num:
#     if i > largest:
#         largest=i
# print("The Largest number:", largest)

# text = "python programming"
# count = 0

# for char in text:
#     if char in "aeiou":
#         count +=1

# print("Number of Vowels:", count)

#While LOOP

# i = 1

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

# print("The number of digits:", count)

# correct_number = 4

# guess = int(input("Enter a number:"))

# while guess != correct_number:
#     print("Wrong Number!!")

#     guess = int(input("Enter a number" ))

# print("Correct Guess!!")


# Loop Control statements

# for i in range(20):
#     if i ==12:
#         break
#     print(i)

# to skip any value  
for i in range(20):
    if i ==12:
        continue
    print(i)


