check = True
while check:
    number = int(input("Enter a number between 10 and 20: \n"))
    if number < 10:
        print("Too low, try again")
    elif number > 20:
        print("Too high, try again")
    elif 10 <= number <= 20:
        print("Thank you")
        check = False
