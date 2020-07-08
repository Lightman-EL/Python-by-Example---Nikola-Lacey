import random

random_number = random.randint(1, 5)
number = int(input("Please, enter a number between 1 and 5: \n"))

while 1 <= number <= 5:
    if number == random_number:
        print("Correct")
    elif number > random_number:
        print("Too high")
        number = int(input("Please, enter a number between 1 and 5: \n"))
        if number == random_number:
            print("Correct")
        else:
            print("You lose")
    elif number < random_number:
        print("Too low")
        number = int(input("Please, enter a number between 1 and 5: \n"))
        if number == random_number:
            print("Correct")
        else:
            print("You lose")
    print("The number was ", random_number)
else:
    print("Error")