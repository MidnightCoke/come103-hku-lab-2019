
CLASS_A = 20
CLASS_B = 15
CLASS_C = 10


def main():

    a_seat = int(input("Enter count of A seats: "))
    b_seat = int(input("Enter count of B seats: "))
    c_seat = int(input("Enter count of C seats: "))
    income(a_seat, b_seat, c_seat)


def income(a, b, c):
    tot = CLASS_A*a+CLASS_B*b+CLASS_C*c
    print("Income from class A seats: ${aseat}".format(aseat=CLASS_A*a))
    print("Income from class B seats: ${bseat}".format(bseat=CLASS_B*a))
    print("Income from class C seats: ${cseat}".format(cseat=CLASS_C*a))
    print("Total Income: ${tot}".format(tot=tot))


main()
