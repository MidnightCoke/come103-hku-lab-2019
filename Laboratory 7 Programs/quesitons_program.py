import random


def main():
    for x in range(1, 6):
        print_quest(x)


def print_quest(a):
    print("Question " + str(a))
    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    print(str(num_1) + " + " + str(num_2) + " = _____")


main()
