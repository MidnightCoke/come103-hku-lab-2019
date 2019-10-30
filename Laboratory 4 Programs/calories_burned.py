
print("Minutes\t    Calories Burned")
print("---------------------------")

TREADMILL_CAL = 4.2

for min in range(5, 61, 5):
    print(min, "\t\t", format(min*TREADMILL_CAL, '.2f'))
