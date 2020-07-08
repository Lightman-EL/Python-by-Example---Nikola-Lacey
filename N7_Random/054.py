import random

choice = input("I throw a coin, choice head or tail (h/t): \n")
rand_choice = random.choice(["h", "t"])

if choice.lower() == rand_choice:
    print("You win!")
else:
    print("Bad luck")

if rand_choice == "h":
    print("It was head")
elif rand_choice == "t":
    print("It was tail")