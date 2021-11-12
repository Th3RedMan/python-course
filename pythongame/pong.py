import turtle  #  Used for basic games for screen and parts
import pygame
player_a = input("Player 1 Please Enter Your Username: ")
player_b = input("Player 2 Please Enter Your Username: ")
game_mode = ""
clock = pygame.time.Clock()
while game_mode == "":
    game_mode = input("Type Your Game Mode: Easy Medium Hard  ").casefold()
    # while "easy" or "medium" or "hard" != game_mode:
    #     game_mode = input("Type Your Game Mode: Easy Medium Hard  ").casefold()

    if "easy" == game_mode:
        initial_speed = 2.5
        length = 5
    elif "medium" == game_mode:
        initial_speed = 3.5
        length = 3
    elif "hard" == game_mode:
        initial_speed = 4
        length = 1
    wn = turtle.Screen()
    wn.title("Pong by @Th3RedMan")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    #  Score
    score_a = 0
    score_b = 0

    #  Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0) #  Speed of animation- max speed
    paddle_a.shape("square") # default 20px by 20px
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=length, stretch_len=1)  #  5 times 20
    paddle_a.penup()
    paddle_a.goto(-350, 0)
    #  Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0) #  Speed of animation- max speed
    paddle_b.shape("square") # default 20px by 20px
    paddle_b.color("white")
    paddle_b.shapesize(stretch_wid=length, stretch_len=1)  #  5 times 20
    paddle_b.penup() #  doesn't leave tracks of move
    paddle_b.goto(350, 0)
    #  Ball
    ball = turtle.Turtle()
    ball.speed(0) #  Speed of animation- max speed
    ball.shape("square") # default 20px by 20px
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = initial_speed #  Delta speed for x
    ball.dy = initial_speed # speed y 2 pixels
    #  Pen

    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("{}: 0  {}: 0".format(player_a, player_b), align="center", font=("courier", 24, "normal"))

    #  Function
    def paddle_a_up():
        y = paddle_a.ycor()  #  finds y coords
        y += 20 #  Add 20 pixles to y coordinate
        paddle_a.sety(y)

    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)

    def paddle_b_up():
        y = paddle_b.ycor()
        y += 20
        paddle_b.sety(y)

    def paddle_b_down():
        y = paddle_b.ycor()
        y -= 20
        paddle_b.sety(y)

    #  Keyboard binding
    wn.listen()  #  Listen for keyboard inputs
    wn.onkeypress(paddle_a_up, "w")
    wn.onkeypress(paddle_a_down, "s")
    wn.onkeypress(paddle_b_up, "Up")
    wn.onkeypress(paddle_b_down, "Down")
    #  Main Game Loop
    while True:
        wn.update()  # everytime loop repeats it updates screen
        clock.tick(60)
        #  Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        #  Border Checking
        if paddle_a.ycor() + 50 > 290:
            paddle_a.sety(240)
        if paddle_a.ycor() - 50 < -290:
            paddle_a.sety(-237)

        if paddle_b.ycor() + 50 > 290:
            paddle_b.sety(240)
        if paddle_b.ycor() - 50 < -290:
            paddle_b.sety(-237)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1  #  reverses
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx = initial_speed
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("{}: {}  {}: {}".format(player_a, score_a, player_b, score_b), align="center", font=("courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx = initial_speed
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("{}: {}  {}: {}".format(player_a, score_a, player_b, score_b), align="center", font=("courier", 24, "normal"))


        #  Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and \
                (ball.ycor() < paddle_b.ycor() +50 and  # TODO: Make an equation to automatically change where hitbox of paddle is
                 ball.ycor() > paddle_b.ycor() - 50):
            ball.setx(340)
            ball.dx *= -1

        if (ball.xcor() < -340 and ball.xcor() > -350) and \
                (ball.ycor() < paddle_a.ycor() +50 and
                 ball.ycor() > paddle_a.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1