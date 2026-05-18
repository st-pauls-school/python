import turtle
import sys

from challenges import CHALLENGES

CELL = 80

_screen        = None
_pen           = None
_cursor        = None
_dots          = {}
_move_count    = 0
_finish_colour = None
_cols          = 0
_rows          = 0


def start(challenge_number):
    global _screen, _pen, _cursor, _dots, _finish_colour, _move_count
    global _cols, _rows

    ch   = CHALLENGES[challenge_number]
    _cols = ch["cols"]
    _rows = ch["rows"]
    _dots = ch["dots"]
    _finish_colour = ch["finish"]
    _move_count    = 0
    start_col, start_row = ch["start"]
    cols, rows = _cols, _rows

    _screen = turtle.Screen()
    _screen.bgcolor("white")
    _screen.title(f"Challenge {challenge_number}: {ch['goal']}")
    _screen.setup(cols * CELL + CELL, rows * CELL + CELL)
    _screen.tracer(0)

    _pen = turtle.Turtle()
    _pen.hideturtle()
    _pen.penup()
    _pen.speed(0)

    # grid lines
    _pen.pencolor("#cccccc")
    _pen.pensize(1)
    left_edge  = -CELL // 2
    right_edge = (cols - 1) * CELL + CELL // 2
    bottom     = -CELL // 2
    top        = (rows - 1) * CELL + CELL // 2

    for col in range(cols + 1):
        x = col * CELL - CELL // 2
        _pen.goto(x, bottom); _pen.pendown()
        _pen.goto(x, top);    _pen.penup()

    for row in range(rows + 1):
        y = row * CELL - CELL // 2
        _pen.goto(left_edge, y);  _pen.pendown()
        _pen.goto(right_edge, y); _pen.penup()

    # dots
    for (col, row), colour in _dots.items():
        _pen.goto(col * CELL, row * CELL)
        _pen.dot(50, colour)

    # cursor
    _cursor = turtle.Turtle()
    _cursor.shape("arrow")
    _cursor.penup()
    _cursor.goto(start_col * CELL, start_row * CELL)

    _screen.tracer(1)

    print(f"Challenge {challenge_number}: {ch['goal']}")


def _try_move(dcol, drow):
    global _move_count
    col = (round(_cursor.xcor() / CELL) + dcol) % _cols
    row = (round(_cursor.ycor() / CELL) + drow) % _rows
    _move_count += 1
    _cursor.goto(col * CELL, row * CELL)

def move_right(): _try_move( 1,  0)
def move_left():  _try_move(-1,  0)
def move_up():    _try_move( 0,  1)
def move_down():  _try_move( 0, -1)


def colour_here():
    col = round(_cursor.xcor() / CELL)
    row = round(_cursor.ycor() / CELL)
    return _dots.get((col, row), "none")


def _count_code_lines():
    try:
        with open(sys.argv[0]) as f:
            lines = f.readlines()
        in_section = False
        count = 0
        for line in lines:
            stripped = line.strip()
            if stripped == "# --- write your code below here ---":
                in_section = True
                continue
            if stripped == "# --- do not change anything below this line ---":
                break
            if in_section and stripped and not stripped.startswith("#"):
                count += 1
        return count
    except Exception:
        return None


def done():
    on_finish = colour_here() == _finish_colour
    print(f"\n{'Challenge complete!' if on_finish else 'Not quite!'}")
    print(f"  Finished on {_finish_colour}: {'yes' if on_finish else 'no'}")
    print(f"  Moves made:    {_move_count}")
    written_lines = _count_code_lines()
    if written_lines is not None:
        print(f"  Lines written: {written_lines}")
    turtle.done()
