from random import randint

loop = True
my_number = int(input())
i = 0

while loop:
    computer_guess = randint(0, 100)
    i = i + 1
    if computer_guess == my_number:
        print("computer_guess= ", computer_guess)
        print("congrats")
    elif computer_guess < my_number:
        print("computer_guess", computer_guess)
        print("larger")
        computer_guess = randint(computer_guess, 100)
    else :
        print("computer_guess ", computer_guess)
        print("smaller")
        computer_guess = randint(0, computer_guess)
    if i > 8:
        print("game over")
        loop = False


