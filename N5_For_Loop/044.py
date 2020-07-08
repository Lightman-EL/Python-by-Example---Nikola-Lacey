guests = int(input("How many guests you want to invite: \n"))
if guests < 10:
    for i in range(1, guests + 1):
        print(i, ")")
        name = input("Please, enter  guest name: \n")
        print(name.title(), " has been invited")
elif guests > 10:
    print("Too many people")
else:
    print("I don't understand")