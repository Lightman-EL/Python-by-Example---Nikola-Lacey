pass1 = input("Enter a new password: \n")
pass2 = input("Conform the password: \n")

if pass1 == pass2:
    print("Thank you")
elif pass1.lower() == pass2.lower():
    print("They must be in the same case")
else:
    print("Incorrect")