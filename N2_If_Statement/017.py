age = int(input("How old are you? \n"))
if 200 >= age >= 18:
    print("You can vote")
if age == 17:
    print("You can learn to drive")
if age == 16:
    print("You can buy a lottery ticket")
if 0 <= age < 16:
    print("You can go Trick-orTreating")
else:
    print("Incorrect age")