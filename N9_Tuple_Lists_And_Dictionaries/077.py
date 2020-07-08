guests = []
loop = True

for i in range(1, 4):
    invited = input("Enter the names of guest: \n")
    guests.append(invited.title())

while loop:
    invited_loop = input("Are you want add another? \n")
    if invited_loop.lower() == "no":
        break
    else:
        guests.append(invited_loop.title())

print("You have invited ", len(guests), " guests")
print(guests)
name = input("Enter a name: ")
name = name.title()
if name in guests:
    person_index = guests.index(name)
    print(person_index)
    delete = input("Do you want still that person to come to the party? \n")
    if delete.lower() == "no":
        del guests[person_index]
    else:
        print("OK")
else:
    print("There're no this name")

print(guests)