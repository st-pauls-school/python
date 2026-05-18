import pgzrun

WIDTH  = 7 * 80   # 560
HEIGHT = 7 * 80   # 6 rows + 1 preview row at top

COLS, ROWS = 7, 6
CELL, RADIUS = 80, 32

EMPTY, RED, YELLOW = 0, 1, 2

COLOURS = {
    EMPTY:  (200, 200, 220),
    RED:    (220,  50,  50),
    YELLOW: (230, 210,   0),
}

grid = [[EMPTY] * COLS for _ in range(ROWS)]
current_player = RED
hover_col = 0

def draw():
    screen.fill((30, 30, 180))                              # blue grid
    screen.draw.filled_rect(Rect(0, 0, WIDTH, CELL), (40, 40, 40))  # top strip

    # preview piece following the mouse
    px = hover_col * CELL + CELL // 2
    screen.draw.filled_circle((px, CELL // 2), RADIUS, COLOURS[current_player])

    # grid circles
    for row in range(ROWS):
        for col in range(COLS):
            x = col * CELL + CELL // 2
            y = (row + 1) * CELL + CELL // 2
            screen.draw.filled_circle((x, y), RADIUS, COLOURS[grid[row][col]])

def on_mouse_move(pos):
    global hover_col
    hover_col = min(pos[0] // CELL, COLS - 1)

def on_mouse_down(pos):
    col = pos[0] // CELL
    if 0 <= col < COLS:
        drop(col)

def drop(col):
    global current_player
    for row in range(ROWS - 1, -1, -1):         # find lowest empty row
        if grid[row][col] == EMPTY:
            grid[row][col] = current_player
            current_player = YELLOW if current_player == RED else RED
            return

