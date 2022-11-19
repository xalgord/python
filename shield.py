import turtle
import math

kachhua = turtle.Turtle()

wn = turtle.Screen()
wn.bgcolor("#000042")


def func1(x, y):
    kachhua.penup()
    kachhua.goto(x, y)
    kachhua.pendown()
    kachhua.setheading(0)
    kachhua.pensize(2)
    kachhua.speed(10)


def func2(r, color):
    x_point = 0
    y_pont = -r
    func1(x_point, y_pont)
    kachhua.pencolor(color)
    kachhua.fillcolor(color)
    kachhua.begin_fill()
    kachhua.circle(r)
    kachhua.end_fill()


def func3(r, color):
    func1(0, 0)
    kachhua.pencolor(color)
    kachhua.setheading(162)
    kachhua.forward(r)
    kachhua.setheading(0)
    kachhua.fillcolor(color)
    kachhua.begin_fill()
    for i in range(5):
        kachhua.forward(math.cos(math.radians(18)) * 2 * r)  # 2cos18°*r
        kachhua.right(144)
    kachhua.end_fill()
    kachhua.hideturtle()


if __name__ == '__main__':
    func2(288, '#AA1428')
    func2(234, '#FFFFFF')
    func2(174, '#AA1428')
    func2(114, '#000042')
    func3(114, '#FFFFFF')
    turtle.done()
