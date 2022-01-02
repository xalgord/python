import turtle
import ui

def write(self,text, move=True, align="center", font=None):
        text = str(text)
        w, h = ui.measure_string(text)
        color = "self._current_color"
        pos = self._pos
        def _draw():
            ui.draw_string(text, (pos.x, pos.y - h, 0, 0),color=color)
        self._add_drawing(_draw)
        if move:
            self._pos += (w, 0)
        self.update_view()

pen = turtle.Turtle()
pen.color("#FFFFFF")
turtle.Screen().bgcolor("#1C1C1C")

def draw_i():
	pen.speed(1)
	pen.forward(50)
	pen.backward(25)
	pen.right(90)
	pen.forward(140)
	pen.left(90)
	pen.forward(25)
	pen.backward(50)

# define functions to draw things
def love(fill='pink'):
	# draw love
	pen.fillcolor(fill)
	pen.begin_fill()

	pen.left(50)
	pen.forward(100)
	pen.circle(40, 180)
	pen.left(260)
	pen.circle(40, 180)
	pen.forward(100)
	pen.end_fill()

def draw_u():
	pen.up()
	pen.left(90)
	pen.forward(170)
	pen.right(130)
	pen.backward(25)
	pen.down()        # start drawing
	pen.forward(100)
	pen.circle(40, 180)
	pen.forward(100)

def stickman(gender='m'):
	# stickman
	pen.right(60)
	pen.forward(50)
	pen.left(120)
	pen.forward(50)
	pen.backward(50)
	pen.right(150)
	pen.forward(60)

	pen.right(120)
	pen.forward(50)
	pen.backward(50)
	pen.right(180)

	pen.left(60)
	pen.forward(50)
	pen.backward(50)

	pen.right(210)

	if gender == 'f':
		# draw female head
		pen.forward(30)
		pen.left(90)
		pen.forward(10)
		pen.circle(30, 180)
		pen.forward(10)
		pen.left(90)
		pen.forward(30)
		return

	# draw male head
	pen.circle(20, 360)
	#pen.write(" I")


# start drawing
pen.pensize(6)
pen.speed(1)

# go some place to draw I
pen.up()  # take the pen up
pen.left(180)
pen.forward(130)
pen.down()       # start drawing


# i
draw_i()

# go home/center
pen.up()
pen.home()
pen.down()

# draw love
love('#FFCC00')


# U
draw_u()

# go home/center
pen.up()
pen.home()

# go to new location (down)
pen.fillcolor('white')
pen.right(90)
pen.forward(170)
pen.left(90)
pen.down()

pen.up()  # take the pen up
pen.left(180)
pen.forward(130)
pen.down()       # start drawing

stickman()      # make male stick character

# place for stick woman
pen.up()
pen.forward(350)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.down()

stickman(gender='f')  # make female stick character

# place to draw love (another one)
pen.up()
pen.home()
pen.right(90)
pen.forward(170)
pen.left(90)
pen.down()
love('red')

# message
pen.up()
pen.left(142)
pen.forward(65)
pen.write("Can You?\n       💕", font=('Arial', 14, 'bold'), move=True, align="center")

pen.home()
pen.up()
pen.right(90)
pen.forward(300)
pen.write("Programmed by xalgord\n", font=('Arial', 10, 'bold'), move=True, align="center")
pen.hideturtle()

pen.screen.exitonclick()  # shows the graphics untill we exit
