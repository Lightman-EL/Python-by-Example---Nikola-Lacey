name = input("Enter your name: \n")
print("That has", len(name), " characters in it")
surname = input("Enter your surname: \n")
print("That has", len(surname), " characters in it")
full_name = name.title() + " " + surname.title()
print("That has", len(full_name), " characters in it")
print(len(full_name))