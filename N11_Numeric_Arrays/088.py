from array import *

numbers = array('i', [])

for i in range(1, 6):
    number = int(input("Enter a number: \n"))
    numbers.append(number)

numbers = sorted(numbers)
print(numbers)