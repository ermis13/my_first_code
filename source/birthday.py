import turtle
from turtle import *

wn = Screen()
wn.bgcolor('black')
t= turtle.Turtle()
t.speed(0)
t.pencolor('white')

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()

def write(message,pos):
    x,y=pos
    t.penup()
    t.goto(x,y)
    t.color('white')
    style=('Stencil Std', 18, 'bold')
    t.write(message,font=style)

write("Happy Birthday", (-85, -40))

write("I", (-68,95))
write('L',(-55,95))
write('O',(-42,95))
write('V',(-26,95))
write('E',(-10,95))
write('Y',(10,95))
write('O',(26,95))
write('U',(45,95))

wn.mainloop()

wn.mainloop()
