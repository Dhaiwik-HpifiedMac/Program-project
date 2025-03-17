import turtle
 t = turtle.Turtle()
 t.goto(0,0)
 screen = turtle.Screen()
 turtle.listen()
  cur_x = 0
  cur_y = 0
  xvel = 0
  yvel = 0
  playing = 0
  intensity = 50
 
  def move_forward():
    yvel = yvel + (playing*intensity)

def move_left():
  xvel = xvel - (playing*intensity)

def move_right():
  xvel = xvel + (playing*intensity)

  def move_backward():
  yvel = yvel - (playing*intensity)

 def frame():
    cur_x = cur_x + xvel
    cur_y = cur-y + yvel
    xvel = xvel/10
    yvel = yvel/10
    player(x,y,50)
 
def player(x,y,r):
 	t.pendown
  t.goto(x-r,y-r)
 	t.forward(2*r)
 	t.right(2*r)
 	t.backward(2*r)
 	t.left(2*r)
  t.penup
  
 def switchstate:
     if (playing == 0)
         playing = 1
     if (playing == 1)
         playing = 0
     delay(1)


 while (playing == 1)
     frame()
turtle.onkey(switchstate, "Space") 
turtle.onkey(move_forward, "Up")
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_backward, "Down")
turtle.listen()
