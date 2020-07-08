from array import *

numbers = array('i', [])

while len(numbers) < 5:
    number = int(input("Enter a number: \n"))
    numbers.append(number)

numbers = sorted(numbers)
print(numbers)

deleted_num = int(input("Enter a number that you want to delete: \n"))
if deleted_num in numbers:
    numbers.remove(deleted_num)
else:
    print("Invalid number")

print(numbers)