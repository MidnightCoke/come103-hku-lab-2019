import turtle

turtle.speed(1)


def main():
    x1_axis = int(input("Enter the x1 axis"))
    y1_axis = int(input("Enter the y1 axis"))
    x2_axis = int(input("Enter the x2 axis"))
    y2_axis = int(input("Enter the y2 axis"))
    x3_axis = int(input("Enter the x3 axis"))
    y3_axis = int(input("Enter the y3 axis"))
    tri_color = input("Enter the color: ")

    draw_tri(x1_axis, y1_axis, x2_axis, y2_axis, x3_axis, y3_axis, tri_color)


def draw_tri(x1, y1, x2, y2, x3, y3, color):

    turtle.fillcolor(color)
    turtle.penup()
    turtle.begin_fill()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()


main()
