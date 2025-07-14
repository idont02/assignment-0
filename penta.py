import turtle
pen = turtle.Turtle()
pen.speed('fastest')
pen.begin_fill()
for i in range(24):
    for i in range(5):
        pen.fd(124)
        pen.left(72)
    pen.right(15)
pen.end_fill()
turtle.Screen().mainloop()
