import random


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,5)
        return first, second



