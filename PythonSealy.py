import turtle
import math
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("black")
screen.title("Sealy - Python Turtle")
t = turtle.Turtle()
t.hideturtle()
t.speed(4)
t.pensize(4)
def polygon(points, fill, outline="black", width=4):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.pensize(width)
    t.color(outline, fill)
    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])
    t.end_fill()
def ellipse(cx, cy, rx, ry, fill, outline="black", width=4):
    points = []
    for i in range(101):
        angle = 2 * math.pi * i / 100
        x = cx + rx * math.cos(angle)
        y = cy + ry * math.sin(angle)
        points.append((x, y))
    polygon(points, fill, outline, width)
def dot(x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.dot(size, color)
body = [
    (-230, 0),
    (-225, 35),
    (-210, 70),
    (-185, 105),
    (-150, 130),
    (-105, 145),
    (-55, 150),
    (0, 145),
    (45, 130),
    (75, 105),
    (105, 80),
    (130, 82),
    (150, 95),
    (170, 105),
    (185, 98),
    (170, 75),
    (155, 55),
    (180, 35),
    (205, 20),
    (220, 0),
    (205, -5),
    (180, -8),
    (165, -25),
    (185, -45),
    (175, -65),
    (150, -78),
    (120, -65),
    (95, -82),
    (60, -95),
    (30, -92),
    (5, -75),
    (-20, -100),
    (-50, -102),
    (-70, -90),
    (-100, -92),
    (-140, -90),
    (-175, -82),
    (-205, -65),
    (-225, -40)
]
polygon(body, "white", "black", 5)
flipper = [
    (-10, -72),
    (10, -90),
    (25, -105),
    (10, -112),
    (-12, -108),
    (-30, -94),
    (-35, -78)
]
polygon(flipper, "white", "black", 5)
ellipse(-150, 15, 38, 25, "#bcefff", "black", 3)
dot(-185, 45, 25, "black")
dot(-110, 45, 25, "black")
dot(-190, 8, 22, "#ffb6c9")
dot(-105, 8, 22, "#ffb6c9")
dot(-148, 18, 11, "black")
t.penup()
t.goto(-165, 10)
t.pendown()
t.color("black")
t.pensize(4)
t.goto(-158, 0)
t.goto(-148, -4)
t.goto(-138, 0)
t.goto(-130, 10)
tongue = [
    (-153, -3),
    (-148, -15),
    (-140, -18),
    (-134, -12),
    (-137, -3)
]
polygon(tongue, "#ff8fa8", "black", 3)
t.penup()
t.goto(-150, 20)
t.pendown()
t.color("black")
t.pensize(3)
t.goto(-153, 12)
t.penup()
t.goto(0, -280)
t.color("white")
t.write(
    "Sealy 🦭",
    align="center",
    font=("Arial", 24, "bold")
)

turtle.done()
