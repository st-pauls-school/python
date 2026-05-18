import turtle

CELL = 80
COLS = 5
ROWS = 4

screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(COLS * CELL + CELL, ROWS * CELL + CELL)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed(0)

# ── draw grid lines ───────────────────────────────────────────────────────
pen.pencolor("#cccccc")
pen.pensize(1)

left_edge  = -CELL // 2
right_edge = (COLS - 1) * CELL + CELL // 2
bottom     = -CELL // 2
top        = (ROWS - 1) * CELL + CELL // 2

for col in range(COLS + 1):
    x = col * CELL - CELL // 2
    pen.goto(x, bottom); pen.pendown()
    pen.goto(x, top);    pen.penup()

for row in range(ROWS + 1):
    y = row * CELL - CELL // 2
    pen.goto(left_edge, y);  pen.pendown()
    pen.goto(right_edge, y); pen.penup()

# ── draw coloured dots ────────────────────────────────────────────────────
dots = {(0,0):"red", (2,0):"yellow", (4,1):"blue", (1,2):"yellow", (3,3):"red"}

for (col, row), colour in dots.items():
    pen.goto(col * CELL, row * CELL)
    pen.dot(50, colour)

# ── cursor ────────────────────────────────────────────────────────────────
cursor = turtle.Turtle()
cursor.shape("arrow")
cursor.penup()
cursor.goto(0, 0)
screen.tracer(1)

def move_right(): cursor.goto(cursor.xcor() + CELL, cursor.ycor())
def move_left():  cursor.goto(cursor.xcor() - CELL, cursor.ycor())
def move_up():    cursor.goto(cursor.xcor(), cursor.ycor() + CELL)
def move_down():  cursor.goto(cursor.xcor(), cursor.ycor() - CELL)

def colour_here():
    col = round(cursor.xcor() / CELL)
    row = round(cursor.ycor() / CELL)
    return dots.get((col, row), "none")

# ── students write below here ─────────────────────────────────────────────

def find_yellow():
    while colour_here() != "yellow":
        move_right()

find_yellow()

turtle.done()
