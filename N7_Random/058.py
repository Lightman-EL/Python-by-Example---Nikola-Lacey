import random

total = 0

for i in range(1, 6):
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    result = number_1 + number_2
    answer = int(input(str(number_1) + " + " + str(number_2) + " = "))
    if result == answer:
        print("Right")
        total += 1
    else:
        print("Wrong")
print("Your score: ", total)