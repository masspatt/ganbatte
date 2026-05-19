import turtle
import math

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Semangat!")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

colors = ["red", "orange", "gold", "limegreen", "deepskyblue", "mediumpurple", "hotpink"]

def draw_star(t, x, y, size, color):
    t.penup()
    t.goto(x, y - size)
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size * 2)
        t.right(144)
    t.end_fill()

def draw_burst(t, cx, cy, num_rays, length, color):
    t.penup()
    t.goto(cx, cy)
    t.pendown()
    t.color(color)
    t.width(3)
    for i in range(num_rays):
        angle = 360 / num_rays * i
        rad = math.radians(angle)
        ex = cx + length * math.cos(rad)
        ey = cy + length * math.sin(rad)
        t.penup()
        t.goto(cx, cy)
        t.pendown()
        t.goto(ex, ey)
    t.width(1)

def draw_circle_outline(t, cx, cy, radius, color, width=3):
    t.penup()
    t.goto(cx, cy - radius)
    t.pendown()
    t.color(color)
    t.width(width)
    t.circle(radius)
    t.width(1)

# Background burst
for i, color in enumerate(colors):
    draw_burst(t, 0, 0, 12, 230 - i * 10, color)

# Concentric circle outlines
for i, color in enumerate(colors):
    draw_circle_outline(t, 0, 0, 60 + i * 20, color, 2)

# Stars around the center
star_positions = [
    (150, 80), (-150, 80), (0, 170),
    (160, -60), (-160, -60), (90, -160), (-90, -160)
]
for idx, (sx, sy) in enumerate(star_positions):
    draw_star(t, sx, sy, 18, colors[idx % len(colors)])

# Central text
t.penup()
t.goto(0, 30)
t.color("#e65c00")
t.write("SEMANGAT!", align="center", font=("Arial", 28, "bold"))

t.goto(0, -10)
t.color("#444444")
t.write("Kamu pasti bisa!", align="center", font=("Arial", 16, "normal"))

t.goto(0, -40)
t.color("#888888")
t.write("Setiap langkah kecil itu berarti.", align="center", font=("Arial", 11, "italic"))

# Small stars at bottom
small_stars = [(-60, -100), (0, -110), (60, -100)]
for idx, (sx, sy) in enumerate(small_stars):
    draw_star(t, sx, sy, 10, colors[idx * 2 % len(colors)])

turtle.done()
