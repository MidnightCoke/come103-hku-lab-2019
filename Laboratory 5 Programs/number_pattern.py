
lastNumber = int(input("Enter the number: "))
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
for row in range(lastNumber, 1, -1):
    for column in range(1, row):
        print(column, end=' ')
    print("")
