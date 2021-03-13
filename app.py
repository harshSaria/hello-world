# part 1 -------- printing
# print("My name is Harsh Saria")
# print('o----')
# print(' ||||')
# print('*' * 10)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 2 ----- variables
# price = 10
# print(price)
# price = 100
# print(price)
# rating = 0.4
# name = "Harsh"
# is_published = True
# age = 18
# is_new = True
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 3 --------- input from user
# name = input('Whats ur name? ') input takes as a string;so for arithmetic op we need to convert it to int or float
# print('Hi ' + name)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 4----------
# birth_year = input('Birth Year: ')
# print(type(birth_year)) type is used to display the type of the value
# #age = 2021 - birth_year ---- showed an error as it will read 2021 - '2002' which is illogical
# age_correct = 2021 - int(birth_year)
# print(type(age_correct))
# pint(age_correct)
# homework program
# weight_lb = input("Enter your weight in pounds: ")
# weight_kg = 0.453592 * float(weight_lb)
# print(weight_kg)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 5--------- strings
# course = "python code for noobs"
# print(course)
# #course_new = ''python's code for noobs'
# course_new = "'python's code for noobs"
# print(course_new)
# #course_newer = "python code for "noobs""
# course_newer = 'python code for "noobs"'
# print(course_newer)
# print('''
# Hi there.
# This is a multiline string .
# Thank you for teaching me this.
# ''') multi line print
# print(course[0]) # first char
# print(course[-1]) # last char
# print(course[0:3]) # displays 0 1 2
# print(course[0:]) # displays from 0 till last
# print(course[1:]) # displays from 1 to last
# print(course[:3]) # python will interpret it as [0:3]
# copy_of_course = course[:] # creates a copy
# print(copy_of_course)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 6 ------------- formatted string
# first = 'Harsh'
# last = 'Saria'
# # message = first + ' [' + last + '] is in aerospace branch' # not ideal way
# message = f'{first} [{last}] is in aerospace branch' # formatted string
# print(message)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 7 ---------- string method
# course = 'python for noobs'
# print(len(course)) # calculates length of the string including whitespaces
# print(course.upper())
# print(course.find('o')) # displays the index when the given char occurs for the first time
# print(course.replace('noobs' , 'nerds'))
# print('Python' in course) # gives false as its python not Python in the give code
# print('python' in course) # gives true
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 8 ---------------- arithmetic operations
# print(2+3)
# print(2*3)
# print(2/3) # floating
# print(2//3) # integer
# print(10%3)
# print(2**3) # exponent
# # print(2***3) wont give cube
# x=10
# x+=3 # augmented assignment operator
# print(x)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 9 ------- operators precedence
# x = 10 + 3 * 2
# print (x)
# parenthesis > exponent > multi or div > add or sub
# x = 10 + 3 * 2 ** 2
# print(x)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 10 ----------- math functions
# x = 2.9
# print(round(x))
# print(abs(-x))
# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 11 --------- if statements
# is_hot = True
# is_cold = True
# if is_hot:
#   print("It's a hot day")
#   print("Drink plenty of water")
# elif is_cold:
#    print("It's a cold day")
#   print("Wear warm clothes")
# else:
#    print("It's a lovely day")
# print("Enjoy your day")
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#    down_payment = 0.1 * price
# else:
#    down_payment = 0.2 * price
# print(f"Down payment: ${down_payment}")
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 12 -------- logical operators
# has_high_income = True
# has_good_credit = False

# if has_good_credit and has_high_income:
#    print("Eligible for loan")
# elif has_good_credit or has_high_income:
#    print("Not eligible for loan")
# elif has_high_income and not has_good_credit:
#    print("Eligible fo loan")
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 13 ------- comparison operators
# temp = 30
# if temp > 30:
#     print("Hot day")
# else:
#     print("Not a hot day")
# name = input("Enter your name: ")
# if len(name) < 3:
#     print("Too less")
# elif len(name) > 50:
#     print("Too long")
# else:
#     print("Just right")
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 14 ---------- project 1 ------- weight converter
# weight = input('Enter your weight without unit: ')
# response = input('Type L or l if the unit is lbs and type K or k if the unit is kilograms: ')
# if response == 'k' or response == 'K':
#     weight = 2.204623 * float(weight)
#     print(f'You are {weight} pounds')
# elif response == 'l' or response == 'L':
#     weight = float(weight) * 0.453592
#     print(f'You are {weight} kilograms')
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 15 ---- while loops
# i = 1
# while i<=5:
#     print(i * '@')
#     i+=1
# print("Done")
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 16 --------- guessing game
# i = 1
# while i < 4:
#     choice = int(input("guess: "))
#     i+=1
#     if choice == 9:
#         print("you won")
#         break
# else:
#     print("you failed")
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 17 -------- car game
# inp = ""
# started = False
# while True:
#     inp = input('> ').lower()
#     if inp == 'help':
#         print('''
# 1 - start
# 2 - stop
# 3 - quit
#         ''')
#     elif inp == 'start':
#         if started:
#             print("Already started")
#         else:
#             started = True
#             print("started")
#     elif inp == 'stop':
#         if not started:
#             print("Already stopped")
#         else:
#             started = False
#             print("stopped")
#     elif inp == 'quit':
#         break
#     else:
#         print("not recognized")
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 18 ----------- for loops
# for item in 'python':
#     print(item)
# for item in ['Harsh' , 'Saria']:
#     print(item)
# for item in [1, 2, 3, 4]:
#     print(item)
# for item in range(15): # will print 0 to 14
#     print(item)
# for item in range(5, 10): # will print 5 6 7 8 9
#     print(item)
# for item in range(5, 15, 2): # will print 5 7 9 11 13
#     print(item)
# prices = [10, 20, 30]
# sum = 0
# for item in prices:
#     sum += item
# print(f'total is : {sum} ')
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 19 --------------------- nested loops
# for x in range(4):
#     for y in range(3):
#         print(f'({x},{y})')

# solution 1 for printing F
# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     print('x' * x)

# solution 2 for the same problem
# numbers = [5, 2, 5, 2, 2]
# for x in numbers:
#     output = ' '
#     for y in range(x):
#         output += 'x'
#     print(output)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 20 ------------------- lists
# names = ['Harsh' , 'Ankita' , 'Sunita' , 'Sanjay' , 'Ganesha']
# print(names)
# numbers = [1,2,34,5,100,0,-23]
# max = numbers[0]
# for num in numbers:
#     if num > max:
#         max = num
#     else:
#         max = max
# print(max)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 21 -------------------- 2D lists
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 22 ------------------ list methods
# num = [1, 2, 3, 4]
# num.append(45)
# print(num)
# num.insert(2,45)
# print(num)
# num.remove(45)
# print(num)
# num.clear()
# print(num)
# print(45 in num)
# numm = num.copy()
# print(numm)
# program to remove duplicates in a list
# numbers = [1, 2, 3, 3, 4]
# uniques = []
# for num in numbers:
#     if num not in uniques:
#         uniques.append(num)
# print(uniques)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 23 ------------------ tuples
# tuples are like lists but we cannot modify them, they ar immutable
# numbers = (1, 2, 3)
# numbers[0] = 10
# print(numbers[0])
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 24 ------------- unpacking
# coordinates = (1, 2, 3)
# w = coordinates[0] * coordinates[1] * coordinates[2] # not a good way
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# x, y, z = coordinates # this is same as prev 3 lines
# print(x,y,z)
# same can also be used with lists
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 25 -------------------- dictionaries
# diff between list and dictionary?
# customer = {} # empty dictionary
# customer = {
#     "name": "Harsh",
#     "age": 30,
#     # "age": 40, ....each key should be unique in a dictionary
#     "is_verified": True
# }
# print(customer["name"]) # case sensitive
# print(customer["bday"]) # will give error message as bday is not the key
# print(customer.get("bday"))# wont give an error message instead will display "none"
# "None" represents an absence of a value
# print(customer.get("bday", "Apr 20 2002")) # instead of "none" will give "Apr 20 2002"
# customer["name"] = "Harsh Saria" # updates the name key
# print(customer["name"])
# customer["bday"] = "Apr 20 2002" # adds a new key
# print(customer["bday"])
# program to take a phone number and display it in words
# phone = input("Phone: ")
# dict = {
#     "1": "one",
#     "2": "two",
#     "3": "three",
#     "4": "four"
# }
# output = " "
# for num in phone:
#     output += dict.get(num,"!") + " "
# print(output)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 26 ------------ emoji converter
# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)": "😊",
#     ":(": "🙁"
# }
# output = " "
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 27 ----------------------- functions
# def greet_user(): # and not from here
#     print("Hi")
#     print("Good morning")
#
#
# print("Start") # compiler starts from here
# greet_user()
# print("Finish")
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 28 ------------------ parameters
# def greet_user(name): # here name is parameter
#     print(f'Hi {name}')
#
#
# your_name = input("Enter your name: ")
# print()
# print("Start")
# greet_user(your_name) # here your_name is argument
# greet_user() # error
# print("Finish")
# ---------------------------------------------------------------------------------------------------------------------------------------------

# part 29 ---------------- keyword arguments
# def greet_user(f_name, l_name):
#     print(f'Hi {f_name} {l_name}')
#
#
# print("Start")
# greet_user("Saria", "Harsh")
# print("Finish")

# def greet_user(f_name, l_name):
#     print(f'Hi {f_name} {l_name}')
#
#
# print("Start")
# greet_user(l_name = "Saria", f_name = "Harsh")  # can inc the readability of the arguments
# print("Finish")

# def greet_user(f_name, l_name):
#     print(f'Hi {f_name} {l_name}')
#
#
# print("Start")
# greet_user("Harsh", l_name = "Saria")  # USE KEYWORD ARGUMENT AFTER POSITIONAL AGRUMENT. THIS IS RIGHT
# print("Finish")

# def greet_user(f_name, l_name):
#     print(f'Hi {f_name} {l_name}')
#
#
# print("Start")
# greet_user(f_name = "Harsh", "Saria")  # WRONG
# print("Finish")
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 30 --------------------------- return statements
# def square(number):
#     return number*number
#
#
# print(square(2))

# def square(number):
#     print(number*number)
#
#
# print(square(2))  # by default all functions return none
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 31 -------------- creating a usable function
# going back to emoji program
# def emoji_convert(inp):
#     words = inp.split(" ")
#     emojis = {
#         ":)": "😀",
#         ":(": "🙁"
#     }
#     output = " "
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
#
#
# inp = input("> ")
# print(emoji_convert(inp))
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 32 --------------------- exceptions (try and except)
# age = int(input("Age: "))
# print(age)  # 0 means success and any thing other means crashed

# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("Number cant be divided by zero")
# except ValueError:
#     print("Invalid value")
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 33 -------------- classes
# class Point:
#     def move(self):
#         print("Move")
#     def draw(self):
#         print("Draw")
#
#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x, point1.y)
# point1.draw()
# point2 = Point()
# point2.x = 1
# print((point2.x))
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 34 -------------- constructor
# class Point:
#     def __init__(self, x, y):  # seld is reference to current object
#         self.x = x
#         self.y = y
#     def move(self):
#         print("Move")
#     def draw(self):
#         print("Draw")
#
#
# point = Point(10, 20)
# print(point.x, point.y)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f' Hi, I am {self.name}')
#
#
# harsh = Person("Harsh")
# harsh.talk()
#
# saria = Person("Saria")
# saria.talk()
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 35 -------------------------------- inheritance
# class Mammal:
#     def walk(self):
#         print("Walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("Bark")
#
#
# class Cat(Mammal):
#     pass
#
#
# dog1 = Dog()
# dog1.walk()
# dog1.bark()
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 36 ----------------------- modules
# module is file with some python code
# import convertors  # imports all the modules
# print(convertors.kg_to_lbs(70))

# from convertors import kg_to_lbs  # imports specific module
# print(kg_to_lbs(100))

# homework
# from utils import find_max
#
# numbers = [1, 2, 3, 4, 5]
# print(find_max(numbers))
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 37 -------------------- packages
# package is a container for multiple modules
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping
# calc_shipping()

# from ecommerce import shipping
# shipping.calc_shipping()
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 38 ---------- generating random values
# import random
# for i in range(3):
#     print(random.random())

# for i in range(3):
#     print(random.randint(10, 20))

# members = ['Harsh', 'Aaquib', 'Abhishek']
# leader = random.choice(members)
# print(leader)

# import random
#
#
# class Dice:
#     def roll(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 39 ------------- files and directories
# from pathlib import Path

# absolute path ------- C:\Program\Microsoft\Docs
# relative path

# path = Path("ecommerce")
# print(path.exists())
# path1 = Path("mails")
# path1.mkdir()
# path1.rmdir()

# from pathlib import Path
# path = Path()
# for file in path.glob('*.py'):
#     print(file)
# -----------------------------------------------------------------------------------------------------------------------------------------------

# part 40 -------------- pypi and pip
