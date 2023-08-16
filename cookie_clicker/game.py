# turtle graphics
import turtle

image = "cookie-cookie-clicker.gif"

wn=turtle.Screen()
wn.title("Cookie clicker by Hermes and Joe")
wn.bgcolor("green")

wn.register_shape(image)
cookie = turtle.Turtle()
cookie.shape(image)
cookie.speed(0)

nr_of_clicks = 0
pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 200)
pen.write(f"clicks: {nr_of_clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global nr_of_clicks
    nr_of_clicks += 1
    pen.clear()
    pen.write(f"clicks: {nr_of_clicks}", align="center", font=("Courier New", 32, "normal"))
cookie.onclick(clicked)

wn.mainloop()
