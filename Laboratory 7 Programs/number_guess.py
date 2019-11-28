import random

secret_num = random.randint(1, 100)

guessed_num = 0


def guess():
    global guessed_num
    guessed_num = int(input("Enter the guess: "))

    return guess_check(guessed_num)


def guess_check(guessed_num1):

    if guessed_num1 == secret_num:
        print("Congratulations! You guessed the right number!")

    elif guessed_num1 < secret_num:
        print("Too low, Try again")
        guess()
    elif guessed_num1 > secret_num:
        print("Too high, Try again")
        guess()


guess()
