from turtle import *
from os import system
from time import sleep
from math import pi


def sp():
    sleep(pi)
def cl():
    system('cls')
def sides(s):
    while True:
        a = input(f'Please enter the {s}: ')
        try:
            a = int(a)
            break
        except ValueError:
            print('Please type an integer.')
            sp()
            cl()
    return a
            

cl()
l = sides('length')
b = sides('breadth')
fc = input('Please enter the fillcolor: ')
sp()
cl()
print('A window is awaiting.')

turtle = Turtle()
turtle.width = 2
turtle.fillcolor(fc)
turtle.begin_fill()
for i in range(2):
    turtle.fd(l)
    turtle.right(90)
    turtle.fd(b)
    turtle.right(90)
turtle.end_fill()
Screen().mainloop()
