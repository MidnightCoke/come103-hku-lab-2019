STARTING_PRICE = 8000

print("Year\t\tProjected Tuition")
print("-"*30)
for x in range(1, 6):
    print(format(x, '<15d'),  "$", format(STARTING_PRICE, '.2f',))
    STARTING_PRICE += STARTING_PRICE * 0.03
