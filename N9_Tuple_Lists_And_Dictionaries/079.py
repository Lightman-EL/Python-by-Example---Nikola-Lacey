nums = []
count = 0

while count < 3:
    num = int(input("Enter a number: \n"))
    nums.append(num)
    print(nums)
    count += 1
last_num = input("Do you want save last number? (y/n)\n")
if last_num.lower() == "n":
    nums.remove(num)
print(nums)