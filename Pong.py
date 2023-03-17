# Simple Pong game
# By TobeyTobes

import turtle
import winsound

win = turtle.Screen()
win.title("Pong by Tobey")
win.bgcolor("black")
win.setup(width=800, height =600)
win.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("#42F7C0")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("#118DFF")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.10
ball.dy = 0.10

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keyboard Bindings
win.listen()
win.onkeypress(paddleA_up, "w")
win.onkeypress(paddleA_down, "s")
win.onkeypress(paddleB_up, "Up")
win.onkeypress(paddleB_down, "Down")

# Main Game Loop
while True:
    win.update()
    
    # Move Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # Border 
    
    # Top and Bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    # Left and Right
    if ball.xcor() > 350:
        scoreA += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        scoreB += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))        
        ball.goto(0, 0)
        ball.dx *= -1
    
    # Paddle and Ball Collisions
    if ball.xcor() < -340 and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)    
    elif ball.xcor() > 340 and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
        ball.dx *= -1    
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
