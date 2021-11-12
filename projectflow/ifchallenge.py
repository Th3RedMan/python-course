name = input("What is your name: ")
age = int(input("What is your age: "))

if 18 <= age < 31:
    print("Welcome to the holiday {}!".format(name))
else:
    print("You are not invited {}!".format(name))