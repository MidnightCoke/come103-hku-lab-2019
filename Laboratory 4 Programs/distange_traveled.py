MPH = int(input("What is the speed of the vehicle in mph? "))
TIME = int(input("How many hours has it traveled?  "))


print("Hour \t Distance-Traveled")
for x in range(1, TIME+1):
    print(x, "\t", format(x*MPH, '.2f'))
