total = 0
check = "y"
while check == "y":
    number = int(input("Enter a number: \n"))
    total += number
    check = input("Do you want add another number: (y)\n")
print("The total is ", total)