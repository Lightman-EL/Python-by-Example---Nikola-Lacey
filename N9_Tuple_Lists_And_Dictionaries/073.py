foods = {}
for i in range(1, 5):
    food = input("Enter your favourite food: \n")
    foods[i] = food
print(foods)

removed = int(input("Which one do you want to remove: \n"))
if removed in foods:
    del foods[removed]
print(sorted(foods.values()))
