number = int(input("1) Square\t 2) Triangle\nEnter a number: \n"))
if number == 1:
    side = int(input("Please enter the length of one side\n"))
    print("The area is ", side ** 2)
elif number == 2:
    base = int(input("Please enter the base of triangle: \n"))
    height = int(input("Please enter the height of triangle: \n"))
    print("The area is ", (base * height) / 2)
else:
    print("You enter invalid number")