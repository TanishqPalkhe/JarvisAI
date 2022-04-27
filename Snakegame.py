from turtle import Screen, Turtle
import time
import random

delay = 0.1
score = 0
highscore = 0
bodies = []
# screen
s = Screen()
s.title("snake game")
s.bgcolor("gray")
s.setup(width=600, height=600)
# snake head
head = Turtle()
head.speed(0)
head.color("black")
head.shape("circle")
head.fillcolor("yellow")
head.goto(0, 0)
head.penup()
head.direction = "stop"
# food
food = Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.fillcolor("red")
food.penup()
food.ht()  # hide the turtle
food.goto(0, 290)
food.st()  # show turtle
# score bord
sb = Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.goto(-250, -250)
sb.penup()
sb.ht()
sb.write("write:0  //  Highest score:0")


def moveup():
    head.direction = "up"


def movedown():
    head.direction = "down"


def moveleft():
    head.direction = "left"


def moveright():
    head.direction = "right"


def movestop():
    head.direction = "stop"


# movement
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.sety(x - 20)
    elif head.direction == "right":
        x = head.ycor()
        head.sety(x + 20)


# event handling onkey is used when user performs function in keyboard or mouse
s.listen()
s.onkey(moveup, "Up")
s.onkey(movedown, "Down")
s.onkey(moveleft, "Left")
s.onkey(moveright, "Right")
s.onkey(movestop, "space")
# main loop
while True:
    s.update()
    if head.xcor() > 290:
        head.setx(-290)
    elif head.ycor() > 290:
        head.sety(-290)
    elif head.xcor() < -290:
        head.setx(290)
    elif head.ycor() < -290:
        head.sety(290)
    # collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        # increase the length of turtle
        body = Turtle()
        body.speed(0)
        body.penup()
        body.color("black")
        body.shape("circle")
        body.fillcolor("yellow")
        bodies.append(body)
        score += 10
        delay -= 0.001
        if score > highscore:
            score = highscore
        sb.clear()
        sb.write("Score: {}  Highest score: {}".format(score, highscore))
    # move the snake body
    for index in range(len(bodies) - 1, 0, -1):
        x = bodies[index - 1].xcor()
        y = bodies[index - 1].ycor()
        bodies[index].goto(x, y)
    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)
    move()
    # collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for body in bodies:
                body.ht()
            body.clear()
            score = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: {}  Highest score: {}".format(score, highscore))
    time.sleep(delay)
s.mainloop()
