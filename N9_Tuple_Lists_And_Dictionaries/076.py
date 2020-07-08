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