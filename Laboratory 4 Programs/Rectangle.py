RECTANGLE_1_WIDTH = float(input("Enter the First Rectangle Width: "))
RECTANGLE_1_HEIGHT = float(input("Enter the First Rectangle Height: "))

RECTANGLE_2_WIDTH = float(input("Enter the First Rectangle Width: "))
RECTANGLE_2_HEIGHT = float(input("Enter the First Rectangle Height: "))

REC_1_AREA = RECTANGLE_1_HEIGHT * RECTANGLE_1_WIDTH

REC_2_AREA = RECTANGLE_2_HEIGHT * RECTANGLE_2_WIDTH

print("Area A:", format(REC_1_AREA, '.2f'))
print("Area B:", format(REC_2_AREA, '.2f'))


if REC_1_AREA > REC_2_AREA:
    print("First Rectangle area is greater than the second rectangle")
elif REC_2_AREA > REC_1_AREA:
    print("Second Rectangle area is greater than the first rectangle")
else:
    print("These two rectangles areas is same.")
