"""
sam =turtle.Turtle()
win= turtle.Screen()
sam.color("red")
sam.begin_fill()
x=1
y=0
sam.forward(50)
while True:
    def su():
        if(x==1):
            sam.Left(90)
        if(x==-1):
            sam.Right(90)
        if(y==-1):
            sam.Right(180)
        sam.forward(50)
        x=0
        y=1
        print("jump")

    def sotto():
        if(x==1):
            sam.Right(90)
        if(x==-1):
            sam.Left(90)
        if(y==1):
            sam.Right(180)
        sam.forward(50)
        x=0
        y=-1
        print("jump")

    def destr():
        if(y==1):
            sam.Right(90)
        if(x==-1):
            sam.Right(180)
        if(y==-1):
            sam.Left(90)
        sam.forward(50)
        x=1
        y=0
        print("jump")

    def sin():
        if(y==1):
            sam.Left(90)
        if(x==1):
            sam.Right(180)
        if(y==-1):
            sam.Right(90)
        sam.forward(50)
        x=-1
        y=0
        print("jump")

    win.listen()
    win.onkey(su, "Up")
    win.onkey(sotto, "Down")
    win.onkey(sin, "Left")
    win.onkey(destr, "Right")

    win.mainloop()
    """

import turtle
sam = turtle.Turtle()
win = turtle.Screen()

sam.begin_fill()
win.bgcolor("red")

def up():
    print(sam.pos())
    sam.forward(50)
    if(sam.ycor() >= 500 or sam.xcor() >= 500 or sam.ycor() <= -500 or sam.xcor() <= -500):
        sam.reset()

def down():
    print(sam.pos())
    sam.backward(50)
    if(sam.ycor() >= 500 or sam.xcor() >= 500 or sam.ycor() <= -500 or sam.xcor() <= -500):
        sam.reset()

def left():
    sam.left(90)
    

def right():
    sam.right(90)
    

win.setup(width=1000, height=1000)
win.listen()
win.onkey(up, "Up")
win.onkey(down, "Down")
win.onkey(left, "Left")
win.onkey(right, "Right")
win.mainloop()