import turtle



wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width= 800, height=700)
wn.tracer(0)


#score
scoreA=0
scoreB=0

#paddle A
padle_a = turtle.Turtle()
padle_a.speed(0)
padle_a.shape("square")
padle_a.color('white')
padle_a.shapesize(stretch_wid=5, stretch_len=1)
padle_a.penup()
padle_a.goto(-350, 0)




#paddle B
padle_b = turtle.Turtle()
padle_b.speed(0)
padle_b.shape("square")
padle_b.color('white')
padle_b.shapesize(stretch_wid=5, stretch_len=1)
padle_b.penup()
padle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.5  
ballydirection = 0.5


#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0  PlayerB: 0" , align="center" , font=("Courier", 24,"normal"))






#functions
def padle_a_up():
    y= padle_a.ycor()
    y += 20
    padle_a.sety(y)

def padle_a_down():
    y= padle_a.ycor()
    y -= 20
    padle_a.sety(y)    

def padle_b_up():
    y= padle_b.ycor()
    y += 20
    padle_b.sety(y)

def padle_b_down():
    y= padle_b.ycor()
    y -= 20
    padle_b.sety(y)     

#keyboard binding

wn.listen()
wn.onkeypress(padle_a_up,'w')
wn.onkeypress(padle_a_down,'s')
wn.onkeypress(padle_b_up,'Up')
wn.onkeypress(padle_b_down,'Down')



#main game loop
while True:
    wn.update()    


    #move the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)
    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1    


    if ball.xcor() >390:
        ball.goto(0, 0)
        ballxdirection*= -1
        scoreA+=1
        pen.clear()
        pen.write(
            f"PlayerA: {scoreA}  PlayerB: {scoreB}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    if ball.xcor() < -390:
        ball.goto(0, 0) 
        ballxdirection*= -1   
        scoreB+=1 
        pen.clear()
        pen.write(
            f"PlayerA: {scoreA}  PlayerB: {scoreB}",
            align="center",
            font=("Courier", 24, "normal"),
        )

    #ball colide
    if (ball.xcor() > 340 and ball.xcor () < 350 )and (ball.ycor() < padle_b.ycor() + 50 and ball.ycor() > padle_b.ycor() - 50):
        ball.setx(340)
        ballxdirection *= -1    


    if (ball.xcor() < -340 and ball.xcor () > -350 )and (ball.ycor() < padle_b.ycor() + 50 and ball.ycor() > padle_a.ycor() - 50):
        ball.setx(-340)
        ballxdirection *= -1    

