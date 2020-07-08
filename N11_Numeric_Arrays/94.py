import random
from array import *

numbers = array('i', [])
check = True

for i in range(1, 6):
    num = random.randint(1, 100)
    numbers.append(num)

print(numbers)

while check:
    number = int(input("Enter a number that you want to delete:'\n"))
    if number in numbers:
        print(numbers.index(number))
        numbers.remove(number)
        break
    else:
        print("Try again")

print(numbers)