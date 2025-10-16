from turtle import *
from math import sin,cos,radians

#position function
def pos_for_letter(x,y,deg):
    t.penup()
    t.goto(x,y)
    t.seth(deg)
    t.pendown()
#circle arc function
def arc(deg,size): #size = size to height_A
    for i in range(deg):
        t.fd(1)
        t.right(size)
#turtle setup
t = Turtle('turtle')
t.speed('fastest')
scr = Screen()
height_A = 110*sin(radians(70))
base_A = 220*cos(radians(70))
# #C
pos_for_letter(-250,-50,225)

arc(270,1)

#A
t.shape('classic')
pos_for_letter(-225,-60,70)

t.fd(110)
t.left(40)
t.back(110)
pos_for_letter((base_A/4)-225,((height_A/2)-60),0)
t.fd(base_A/2)

#L
pos_for_letter(-100,height_A-60,-90)
t.fd(height_A)
t.left(90)
t.fd(base_A)

#E
pos_for_letter(100,height_A-60,180)
for i in range(2):
    t.fd(base_A)
    t.left(90)
    t.fd(height_A/2)
    t.left(90)
    t.fd(base_A)
    t.seth(180)

#B
pos_for_letter(200,height_A-60,-90)
t.fd(height_A)
pos_for_letter(200,height_A-60,0)

for i in range(2):
    arc(90,2)
    t.left(180)
scr.mainloop()
