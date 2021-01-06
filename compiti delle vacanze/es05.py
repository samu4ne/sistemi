import turtle
import time
import random

snake = turtle.Turtle()
win = turtle.Screen()


delay= 0.2


win.bgcolor("green")
snake.shape("square")
snake.direzione = "fermo"  #in questo modo lo stato del verme è fermo
snake.penup()
win.title("Forneris snake")



def movimento():
    print(ciao)
    if snake.direzione == "su":
        y = snake.ycor() #y coordinate of the turtle
        snake.sety(y + 20)
 
    if snake.direzione == "giu":
        y = snake.ycor() #y coordinate of the turtle
        snake.sety(y - 20)
 
    if snake.direzione == "destr":
        x = snake.xcor() #y coordinate of the turtle
        snake.setx(x + 20)
 
    if snake.direzione == "sin":
        x = snake.xcor() #y coordinate of the turtle
        snake.setx(x - 20)



def up():
    if(snake.direzione!="giu"):
        y = snake.ycor() #y coordinate of the turtle
        snake.sety(y + 20)
        snake.direzione= "su"
        if(snake.ycor() >= 500 or snake.xcor() >= 500 or snake.ycor() <= -500 or snake.xcor() <= -500):
            snake.reset()

def down():
    if(snake.direzione!="su"):
        y = snake.ycor() #y coordinate of the turtle
        snake.sety(y - 20)
        snake.direzione= "giu"
        if(snake.ycor() >= 500 or snake.xcor() >= 500 or snake.ycor() <= -500 or snake.xcor() <= -500):
            snake.reset()

def left():
    if(snake.direzione!="destr"):
        x = snake.xcor() #x coordinate of the turtle
        snake.setx(x - 20)
        snake.direzione= "sin"
        if(snake.ycor() >= 500 or snake.xcor() >= 500 or snake.ycor() <= -500 or snake.xcor() <= -500):
            snake.reset()
    

def right():
    if(snake.direzione!="sin"):
        x = snake.xcor() #x coordinate of the turtle
        snake.setx(x + 20)
        snake.direzione= "destr"
        if(snake.ycor() >= 500 or snake.xcor() >= 500 or snake.ycor() <= -500 or snake.xcor() <= -500):
            snake.reset()
    

win.setup(width=1000, height=1000)

while True:
    win.listen()
    win.onkey(up, "Up")
    win.onkey(down, "Down")
    win.onkey(left, "Left")
    win.onkey(right, "Right")
    time.sleep(delay)
    #movimento
