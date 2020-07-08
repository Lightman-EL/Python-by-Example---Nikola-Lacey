import random
from array import *

numbers_1 = array('i', [])
numbers_2 = array('i', [])

while len(numbers_1) < 3:
    number = int(input("Enter a number: \n"))
    numbers_1.append(number)

while len(numbers_2) < 5:
    random_num = random.randint(0, 100)
    numbers_2.append(random_num)

large_array = numbers_1[:] + numbers_2[:]

large_array = sorted(large_array)
for i in large_array:
    print(i)
