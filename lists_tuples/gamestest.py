import random
name = input("Please enter your username: ")
print("Hello {}".format(name))
game = (input("Would you like to play a game? yes or no ")).casefold()
play = "yes"
highest = 10
answer = random.randint(1, highest)
guesses = 3


while game != play:
    print("Wrong Choice")
    game = (input("Would you like to play a game? yes or no ")).casefold()

print("Welcome")
print(answer)
guess = int(input("Pick a number 1-{}: ".format(highest)))

while guess != answer:
    print(answer)
    guesses -= 1
    if guesses >1:
        print("Wrong answer you have {} guesses left".format(guesses))
        guess = int(input("Pick a number 1-{}: ".format(highest)))
    elif guesses == 1:
        print("Wrong answer You have 1 guess left")
        guess = int(input("Pick a number 1-{}: ".format(highest)))
    elif guess != answer and guesses == 0:
        print("You have lost")
        exit()
if guess == answer:
    print("Congratulations you are free to leave")
    leave = input("Would You Like To Quit The Game? Yes or No ").casefold()
    while "yes" != leave != "no":
        leave = input("Would You Like To Quit The Game? Yes or No ")
    while leave == "yes":
        exit()
    while leave == "no":
        break
print("Test")