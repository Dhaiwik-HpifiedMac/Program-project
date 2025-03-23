import turtle
t = turtle.Turtle()
t.goto(0,0)
screen = turtle.Screen()
cur_x = 0
cur_y = 0
x_vel = 0
y_vel = 0
playing = 0
def controls(intensity):
# put control code here


def frame(x,y, xvel, yvel):
	x = x + xvel
	y = y + yvel
	player(x,y,50)

  
def player(x,y,r):
	t.pendown
	t.goto(x-r,y-r)
	t.forward(2*r)
	t.right(2*r)
	t.backward(2*r)
	t.left(2*r)
	t.penup
while playing = 0 
 #add code to be able to switch playing 
while playing = 1
#code to switch playing
#run framw
