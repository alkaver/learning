import turtle

wn=turtle.Screen()
wn.title("PING PONG")
wn.bgcolor("black")
wn.setup(800,600)
wn.tracer(0)
game=True
#Score
scoreA=0
scoreB=0
#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.top=50
paddle_a.bottom=-50


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.5
ball.dy = 0.5


#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("RED")
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write(f"PLAYER A     {scoreA}:{scoreB}     PLAYER B",align="center",font=("Courier",30,"normal"))


#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y=y+20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y=y-20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y=y+20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y=y-20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#MAIN
while game==True:
    wn.update()

    #BALL MOVEMENT
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #BORDER CHECKING
    if ball.ycor()==290 or ball.ycor()==-290:
        ball.dy = ball.dy*(-1)
    if ball.xcor()==390 :
        scoreA +=1
        if scoreA==10:
            pen.clear()
            ball.hideturtle()
            paddle_b.hideturtle()
            paddle_a.hideturtle()
            pen.goto(0,0)
            pen.write(f"PLAYER A WON", align="center", font=("Courier", 60, "normal"))
            wn.exitonclick()
        pen.clear()
        pen.write(f"PLAYER A     {scoreA}:{scoreB}     PLAYER B", align="center", font=("Courier", 30, "normal"))
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor() == -390:
        scoreB += 1
        if scoreB==10:
            pen.clear()
            ball.hideturtle()
            paddle_b.hideturtle()
            paddle_a.hideturtle()
            pen.goto(0,0)
            pen.write(f"PLAYER B WON", align="center", font=("Courier", 60, "normal"))
            wn.exitonclick()
        pen.clear()
        pen.write(f"PLAYER A     {scoreA}:{scoreB}     PLAYER B", align="center", font=("Courier", 30, "normal"))
        ball.goto(0,0)
        ball.dx *= -1

    #PADDLE CHECKING
    if ball.xcor() < -340 and ball.xcor() > -350  and ball.ycor() < paddle_a.ycor()+60 and ball.ycor() > paddle_a.ycor()-60:
        ball.setx(-340)
        ball.dx*=-1
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60:
        ball.setx(340)
        ball.dx *=-1







