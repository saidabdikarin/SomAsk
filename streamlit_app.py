import turtle
import datetime

def draw_hand(position, length, width):
    """Draws a hand on the turtle screen."""
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.width(width)
    turtle.right(position)
    turtle.forward(length)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.left(position)

def setup_circle(radius, label, labels_count):
    """Sets up a circle with labels for days, months, or years."""
    turtle.penup()
    turtle.right(90)
    turtle.forward(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()
    turtle.left(90)
    turtle.backward(radius)
    turtle.right(90)

    # Place labels
    for i in range(1, labels_count + 1):
        angle = 360 / labels_count * (i - 1)
        turtle.penup()
        turtle.right(angle)
        turtle.forward(radius + 20)
        turtle.write(str(i), align="center")
        turtle.backward(radius + 20)
        turtle.left(angle)

def draw_date_analog():
    today = datetime.datetime.now()
    day = today.day
    month = today.month
    year = int(str(today.year)[-2:])  # Last two digits of the year

    turtle.speed(0)
    turtle.Screen().title("Analog Date Representation")

    # Draw day circle
    setup_circle(100, "Day", 31)
    draw_hand(360 / 31 * (day - 1), 70, 4)

    # Draw month circle
    setup_circle(150, "Month", 12)
    draw_hand(360 / 12 * (month - 1), 120, 6)

    # Draw year circle
    setup_circle(200, "Year", 100)
    draw_hand(360 / 100 * (year - 1), 170, 8)

    turtle.hideturtle()
    turtle.done()

draw_date_analog()

