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
b = False
s = True
while True:
    a = input(">")
    if a.upper() == "HELP":
        print("start - car is ready to start")
        print("stop  - the car is going to stop")
        print("quit  - end the game")
    elif a.upper() == "START":
        if b:
            print("car already started")
        else:
            b = True
            s = False
            print("the car is ready to start")
    elif a.upper() == "STOP":
        if s:
            print("the car has already stopped")
        else:
            s = True
            b = False
            print("the car stopped")
    elif a.upper() == "QUIT":
        break

    else:
        print("i do not understand that ...")
