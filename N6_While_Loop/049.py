counts = 0
compnum = 50
while compnum == 50:
    number = int(input("Enter a number: \n"))
    counts += 1
    if number > 50:
        print("Too high")
    elif number < 50:
        print("Too low")
    elif number == compnum:
        break
print("Well done, you took", counts, " attempts.")