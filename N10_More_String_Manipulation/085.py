count = 0

name = input("Enter your name: \n")
for i in name.lower():
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1
print(count)