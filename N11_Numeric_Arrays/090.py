from array import *

check = True
numbers = array('i', [])
j = 0

while check:
    number = int(input("Enter a number between 10 and 20: \n"))
    j += 1
    if 10 <= number <= 20:
        numbers.append(number)
    else:
        print("Outside the range")

    if j == 5:
        break

print("Thank you")
for i in numbers:
    print(i)