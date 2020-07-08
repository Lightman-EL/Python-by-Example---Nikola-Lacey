number = int(input("Enter a number below 50 : \n"))
if number <= 50:
    for i in range(50, number-1, -1):
        print(i)
else:
    print("ERROR")