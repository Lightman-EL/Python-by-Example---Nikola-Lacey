count = 0
check = "y"
while check == "y":
    name = input("Enter name who you want to invite to the party: \n")
    print(name.title(), " has now been invited")
    count += 1
    check = input("Do you want invite someone else: (y/n) \n")
print(count, " people have coming to the party")