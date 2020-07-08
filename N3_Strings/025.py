name = input("What is your name? ")
if len(name) > 5:
    surname = input("What is your surname? ")
    print(surname + name.upper())
elif len(name) >= 5:
    print(name.lower())