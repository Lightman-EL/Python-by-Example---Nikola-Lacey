import random
print("We have RED, GREEN, BLUE, YELLOW, BLACK colors. What color you choose: \n")

check = True
color = random.choice(["red", "green", "blue", "yellow", "black"])

while check:
    user_color = input("What colour you choose: \n")

    if user_color.lower() == color:
        print("Well done")
        check = False
    else:
        if color == "red":
            print("FLOWER")
        elif color == "green":
            print("GRASS")
        elif color == "blue":
            print("SKY")
        elif color == "yellow":
            print("SUN")
        elif color == "black":
            print("NIGGER")