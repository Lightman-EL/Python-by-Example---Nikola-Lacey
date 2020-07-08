colours = ["red", "orange", "yellow", "green", "blue", "dark_blue", "purple", "black", "gray", "brown"]
start_number = int(input("Enter a number between 0 and 4\n"))
if 0 <= start_number <= 4:
    end_number = int(input("Enter a number between 5 and 9\n"))
    if 5 <= end_number <= 9:
        print(colours[start_number:end_number])
    else:
        print("Error")
else:
    print("Error")