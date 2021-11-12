choice =  "-"
while choice != "0":

    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo Outside")
        print("4:\tSpend time with family")
        print("0:\tQuit")

    choice = input()
