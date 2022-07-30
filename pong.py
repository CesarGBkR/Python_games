import turtle

# Frame
wn = turtle.Screen()
wn.title("Pog")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player1: 0       Player2: 0", align = "center", font = ("Courier", 24, "normal"))

# Player A

playerA = turtle.Turtle()
playerA.speed(0)
playerA.shape("square")
playerA.color("white")
playerA.penup()
playerA.goto(-350, 0)
playerA.shapesize(stretch_len=1, stretch_wid=5)

# PLayer B
playerB = turtle.Turtle()
playerB.speed(0)
playerB.shape("square")
playerB.color("white")
playerB.penup()
playerB.goto(350, 0)
playerB.shapesize(stretch_len=1, stretch_wid=5)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

# Divisor line
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)


# Functions P.A

def playerA_up():
    y = playerA.ycor()
    y+= 20
    playerA.sety(y)

def playerA_down():
    y = playerA.ycor()
    y-= 20
    playerA.sety(y)

# Functions P.B

def playerB_up():
    y = playerB.ycor()
    y+= 20
    playerB.sety(y)

def playerB_down():
    y = playerB.ycor()
    y-= 20
    playerB.sety(y)

# Keys P.A
wn.listen()
wn.onkeypress(playerA_up, "w")
wn.onkeypress(playerA_down, "s")
# Keys P.B
wn.onkeypress(playerB_up, "Up")
wn.onkeypress(playerB_down, "Down")


while True:

    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border
    if ball.ycor() > 290:
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.dy *= -1

    # Goal
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        score.clear()
        score.write("Player1: {}       Player2: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        score.clear()
        score.write("Player1: {}       Player2: {}".format(scoreA, scoreB), align = "center", font = ("Courier", 24, "normal"))

    # Collisión

    if ((ball.xcor() > 340 and ball.xcor() < 350)
            and (ball.ycor() < playerB.ycor() + 50
            and ball.ycor() > playerB.ycor() -50)):
            ball.dx *= -1
            

    if ((ball.xcor() < -340 and ball.xcor() > -350)
            and (ball.ycor() < playerA.ycor() + 50
            and ball.ycor() > playerA.ycor() -50)):
            ball.dx *= -1
