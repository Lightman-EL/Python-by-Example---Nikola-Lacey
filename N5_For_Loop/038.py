name = input("What is your name? \n")
number = int(input("Enter repetition time: \n"))
for i in range(1, number+1):
    for i in range(0, len(name)):
        print(name[i].upper())