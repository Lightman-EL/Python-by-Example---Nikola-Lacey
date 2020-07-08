total = 0
for i in range(1, 6):
    number = int(input("Enter a number: "))
    includ = input("Do you want that number included? (y/n)\n")
    if includ.lower() == "y":
        total = total + number
print("The total is ", total)
