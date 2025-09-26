from turtle import *

turtle = Turtle()
screen = Screen()
def penta():
    for i in range(5):
        turtle.fd(100)
        turtle.left(360/5)

penta()
turtle.penup()
turtle.goto(200,0)
turtle.pendown()
penta()
screen.mainloop()
