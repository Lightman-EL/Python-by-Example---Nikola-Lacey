import math
number = int(input("Please, enter a number over 500: \n"))
if number >= 500:
    print(round(math.sqrt(number), 2))
else:
    print("Incorrect")