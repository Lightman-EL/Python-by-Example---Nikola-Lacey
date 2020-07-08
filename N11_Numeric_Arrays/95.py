import random
from array import *

numbers = array('f', [])
check = True

for i in range(1, 6):
    num = random.randint(10.0, 100.0)
    numbers.append(num)

print(numbers)

while check:
    number = float(input("Enter a number between 2 and 5: \n"))
    if 2 <= number <= 5:
        for i in numbers:
            print(round(i / number, 2))
        break
    else:
        print("Invalid number")