number = int(input("Enter a number between 1 and 12: \n"))
if 1 <= number <= 12:
    for i in range(1, 11):
        print("\t", number, " * ", i, " = ", number * i)
else:
    print("ERROR!!!!")