numbers = [123, 456, 789, 741]
for number in numbers:
    print(number)
input_number = int(input("Enter a number: \n"))
if input_number in numbers:
    print("This number in ", numbers.index(input_number))
else:
    print("That not in the list")