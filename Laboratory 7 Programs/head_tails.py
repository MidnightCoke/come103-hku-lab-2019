import random


coin_head = 0
coin_tail = 0


def head_tails():
    global coin_head
    global coin_tail
    coin = random.randint(1, 2)
    if coin == 1:
        coin_head += 1
    else:
        coin_tail += 1

    return coin_tail, coin_head


print("HEADS\t\tTAILS\t\tTOTAL")


def repeat():

    for x in range(10000):
        head_tails()


for y in range(1, 11):
    repeat()
    print(format(coin_head, '<15d'), format(coin_tail, '<15d'), y*10000)
