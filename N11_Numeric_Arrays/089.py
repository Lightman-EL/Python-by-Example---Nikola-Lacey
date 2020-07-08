from array import *
import random

numbers = array('i', [])

for i in range(1, 6):
    num = random.randint(0, 100)
    numbers.append(num)

for i in numbers:
    print(i)