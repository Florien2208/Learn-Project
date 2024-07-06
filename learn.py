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

x = (input("phone:"))
digit ={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output=""
for n in x:
    output += digit.get(n,"notfound") + " "
print(output)
