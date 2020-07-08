from array import *

numbers = array('i', [])

while len(numbers) < 5:
    number = int(input("Enter a number: \n"))
    if 10 <= number <= 20:
        numbers.append(number)
    else:
        print("Outside the range")
print("Thank you!")
for i in numbers:
    print(i)
