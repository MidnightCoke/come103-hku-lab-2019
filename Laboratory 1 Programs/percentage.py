MALES = int(input("Enter the numbers of male student: "))
FEMALES = int(input("Enter the numbers of female student: "))

CLASS_SIZE = 100/(int(MALES)+int(FEMALES))

PERCENTAGE_MALES = print("Percentage of Males: ",
                         format(CLASS_SIZE*MALES, '.2f'), "%")
PERCENTAGE_FEMALE = print("Percentage of Females: ",
                          format(CLASS_SIZE*FEMALES, '.2f'), "%")
