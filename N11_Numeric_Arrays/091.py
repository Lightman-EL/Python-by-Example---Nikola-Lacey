from array import *
j = 0
numbers = array('i', [10, 20, 30, 30, 40, 70, 70, 70, 70, 80, 90, 90])
print(numbers)
number = int(input("Enter a number: \n"))
for i in numbers:
    if i == number:
        j += 1

print(j)