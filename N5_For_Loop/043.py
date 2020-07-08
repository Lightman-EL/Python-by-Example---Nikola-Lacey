direction = input("Which direction you want to count (up/down): \n")
if direction.lower() == "up":
    number = int(input("Enter a top number: \n"))
    for i in range(1, number + 1):
        print(i)
elif direction.lower() == "down":
    number = int(input("Enter a number below 20: \n"))
    if number < 20:
        for i in range(number, 0, -1):
            print(i)
    else:
        print("I don't understand")
else:
    print("I don't understand")