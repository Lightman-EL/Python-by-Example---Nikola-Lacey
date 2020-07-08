num = 10
while num > 0:
    print("There are ", num, " green bottles hanging on the wall, \n", num,
          " green bottles hanging on the wall , "
          "\nand if 1 green bottle should accidentally fall.\n")
    num -= 1
    answer = input(" How many green bottles will be hanging on the wall?\n")
    if answer == num:
        print("There will be ", num, " green bottles hanging on the wall")
    else:
        while answer != num:
            answer = int(input("No try again: "))
print("There are no more green bottles hanging on the wall")