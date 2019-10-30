PEN = int(input("Number of pennies: "))
NICKS = int(input("Number of nickels: "))
DIMS = int(input("Number of dimes: "))
QUART = int(input("Number of quarters: "))


TOTAL_MONEY = PEN * 1 + NICKS * 5 + DIMS * 10 + QUART * 25

if(TOTAL_MONEY == 100):
    print("Congrulations, the amount you entered is one dollar !")
elif(TOTAL_MONEY < 100):
    print("Sorry, the amount you entered was less than one dollar")
else:
    print("Sorry, the amount you entered was greater than one dollar.")
