import turtle

turtle.speed(0)

# First Triangle

turtle.fillcolor("green")
turtle.begin_fill()
turtle.goto(0, 0)
turtle.goto(-100, 100)

# Writing Top
turtle.penup()
turtle.goto(0, 100)
turtle.pencolor("green")
turtle.pendown()
turtle.write("TOP", align="center")
turtle.penup()
turtle.goto(-100, 100)

turtle.goto(100, 100)
turtle.goto(0, 0)
turtle.end_fill()
turtle.pencolor("green")


# Second Triangle

turtle.fillcolor("blue")
turtle.begin_fill()
turtle.goto(0, 0)
turtle.goto(-100, -100)
turtle.goto(100, -100)
turtle.goto(0, 0)
turtle.end_fill()

#
turtle.pencolor("blue")
turtle.penup()
turtle.goto(0, -115)
turtle.write("BOTTOM", align="center")
turtle.pendown()


# First Square

turtle.penup()
turtle.goto(-100, 100)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.goto(-200, 0)
turtle.goto(-100, -100)
turtle.goto(0, 0)
turtle.goto(-100, 100)
turtle.end_fill()

# Left Font
turtle.pencolor("black")
turtle.penup()
turtle.goto(-225, -7)
turtle.pendown()
turtle.write("LEFT")

# First Circle

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Second Square

turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(200, 0)
turtle.goto(100, -100)
turtle.goto(0, 0)
turtle.goto(100, 100)
turtle.end_fill()

# Right Font
turtle.pencolor("red")
turtle.penup()
turtle.goto(205, -5)
turtle.pendown()
turtle.write("RIGHT")


# Second Circle

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.hideturtle()

turtle.done()
