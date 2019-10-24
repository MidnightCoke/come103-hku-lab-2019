STARTING_PRINCIPAL = int(input("Enter the starting principal: "))
ANNUAL_INTEREST_RATE = int(input("Enter the annual interest rate: "))
ANNUAL_INTEREST_RATE = ANNUAL_INTEREST_RATE / 100

NUMBER_OF_YEARS = int(
    input("How many times per year is the interest compounded? "))

EARN_INTEREST = int(
    input("For How many years will the account earn interest? "))

END_MONEY = STARTING_PRINCIPAL * \
    (1 + ANNUAL_INTEREST_RATE/NUMBER_OF_YEARS)**(NUMBER_OF_YEARS*EARN_INTEREST)

# Fixed

print("At the end of", EARN_INTEREST,
      "years you will have", format(END_MONEY, ".2f"), "$")
