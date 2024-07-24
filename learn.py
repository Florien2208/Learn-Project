# print("this dj flo Learning python")
# f = input("what is your name? ")
# s = input("what is your favorite color ")
#
# print("hi"+f + "and "+ s)
#
#
# a = input('enter your age? ')
# b = 2024 - int(a)
# print('your age is ', b)
# a = 'hello'
# b = 'flo'
# print(f'{a} dj {b}')
# print(a.upper())
# print(a.find('l'))
# print(a.replace('e','oe'))
# print('el' in a)
# print(20 // 3)
# print(20 ** 4) _#TODO: a random todo 1
# import math
# print(math.floor(6.8))
# a = True
# b = False
# if a and b:
#     print("its very nice")
# a = True
# b = False
# if a and not b:
#     print("its very nice")
# a = int(input('enter the weight'))
# b = input('(L) for pounds (K) for kilos')
# if b.upper() == "L":
#  conver= a*0.45
#  print(f"you are {conver}kilos")
# else:
#  conver = a/0.45
#  print(f"you are {conver} pounds")

#
# i = 0
# while i < 3:
#     y = int(input("gues number but you have three chance:"))
#     i = i + 1
#
#     if y == 9:
#         print("you win !")
#         break
# else:
#  print("you fails")


#     gaming of car
# b = False
# s = True
# while True:
#     a = input(">")
#     if a.upper() == "HELP":
#         print("start - car is ready to start")
#         print("stop  - the car is going to stop")
#         print("quit  - end the game")
#     elif a.upper() == "START":
#         if b:
#             print("car already started")
#         else:
#             b = True
#             s = False
#             print("the car is ready to start")
#     elif a.upper() == "STOP":
#         if s:
#             print("the car has already stopped")
#         else:
#             s = True
#             b = False
#             print("the car stopped")
#     elif a.upper() == "QUIT":
#         break
#
#     else:
#         print("i do not understand that ...")


# for loop
# number = [40, 30, 90, 20, 65]
# total = 0
# for i in number:
#     total += i
# print(f"the total number {total}")

# printing F
#
# number = [5, 2, 5, 2, 2]
# for i in number:
#     output = ''
#     for count in range(i):
#         output += '*'
#     print(output)


# letter L


# numbers=[2,2,2,2,5]
# for i in numbers:
#     output =" "
#     for count in range(i):
#         output += "*"
#     print(output)

# max number
#
# numbers=[8,3,45,89,23,65,98,43,64]
# max= numbers[0]
# for i in numbers:
#     if i >max:
#         max= i
# print(max)
#
# for x in range(4):
#     for y in range(4):
#         for z in range(4):
#             print(f"{x},{y},{z}")


# remove the duplicate

#
# numbers = [3, 6, 8, 2, 6, 9, 7, 5, 3, 4]
# unique=[]
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
# print(unique)
#
# dictionary

# x = (input("phone:"))
# digit ={
#     "1":"one",
#     "2":"two",
#     "3":"three",
#     "4":"four"
# }
# output=""
# for n in x:
#     output += digit.get(n,"notfound") + " "
# print(output)


# using of imojs

#
# x = input(">")
# word = x.split(" ")
# emojis = {
#     ":)": "sad",
#     "(:": "happy"
# }
# output=""
# for n in word:
#     output += emojis.get(n, n) + " "
# print(output)

#
# price =[10, 20, 30,80]
# sum =0
# for i in price:
#     sum = sum + i
# print("the sum is ",sum)


# cordinate =(1,4,5)
# x,y,z,g=cordinate
# print(g)


# function
#
# def user(name):
#     print(f'this is{name}')
#     print('check the point')
#
#
# print('start')
# user("dj flo")
# print("stop")
#
# def emojs_converter(x):
#     word = x.split(" ")
#     emojis = {
#         ":)": "sad",
#         "(:": "happy"
#     }
#     output = ""
#     for n in word:
#         output += emojis.get(n, n) + " "
#     return output
#
#
# x = input(">")
# result = emojs_converter(x)

# classes
#
# class Point:
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(30,70)
# print(p1.y)
#
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def talk(self):
#         print(f"hi am {self.name}")
#
#
# p = Person("john english")
# print(p.talk())
#
# class Mammals:
#     def walk(self):
#         print("walking")
#
#
# class Dog(Mammals):
#     def bark(self):
#         print("barking")
#
#
# class Cat(Mammals):
#     def annoying(self):
#         print("the cat annoying")
#
#
# p1 = Dog()
# p1.walk()
#
# import utils
# numbers = [3, 8, 1, 90, 45, 1]
# print(utils.find_max(numbers))
#
# import random
# names=['john ', 'english', 'flo', 'dj']
# leader = random.choice(names)
# print(leader)

# import utils
#
# dice = utils.Dice()
# print(dice.roll())
from pathlib import Path
path =Path("ecommerce")
print(path.exists())