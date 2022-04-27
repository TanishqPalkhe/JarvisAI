from turtle import Screen, Turtle

DELAY = 100  # milliseconds

def move():
    if direction == 'up':
        y = turtle.ycor()
        turtle.sety(y + 20)
    elif direction == 'down':
        y = turtle.ycor()
        turtle.sety(y - 20)
    elif direction == 'left':
        x = turtle.xcor()
        turtle.setx(x - 20)
    elif direction == 'right':
        x = turtle.xcor()
        turtle.setx(x + 20)

    screen.update()
    screen.ontimer(move, DELAY)

def up():
    global direction
    direction = 'up'

def down():
    global direction
    direction = 'down'

def left():
    global direction
    direction = 'left'

def right():
    global direction
    direction = 'right'

screen = Screen()
screen.title("Hungry Snake Game")
screen.bgcolor('green')
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Turtle()
turtle.shape('square')
turtle.speed('fastest')
turtle.penup()

direction = 'stop'

screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')
screen.listen()

# main game loop

move()

screen.mainloop()