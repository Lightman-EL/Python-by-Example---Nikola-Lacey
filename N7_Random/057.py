import random

random_number = random.randint(1, 10)
correct = True

while correct:

    number = int(input("Please, enter a number between 1 and 10: \n"))

    if number > random_number:
        print("Too high")
    elif number < random_number:
        print("Too low")
    elif number == random_number:
        print("You guess")
        correct = False
