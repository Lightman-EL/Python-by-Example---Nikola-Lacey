name = input("Enter your name: \n")
number = int(input("Enter repetition times: \n"))
if number <= 10:
    for i in range(1, number + 1):
        print(name.title())
else:
    for i in range(1, 4):
        print("Too high")