def fizz_buzz(current):
    """
    Play fizz buzz
    :param current: Number to check
    :return: "Fizz" if current divisible by 3
        "Buzz" if current divisible by 5
        "Fizz Buzz" if current divisible by both 3 and 5
    """
    if current % 3 == 0:
        return "fizz"
    elif current % 5 == 0:
        return "buzz"
    elif current % 15 == 0:
        return "fizz buzz"
    else:
        return str(current)


input("Play Fizz Buzz.  Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lost!  Correct answer was {}".format(correct_answer))
        exit()
else:
    print("Well done, you reached {}".format(next_number))