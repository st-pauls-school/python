CHALLENGES = {
    1: {
        "cols": 4, "rows": 1,
        "start": (0, 0),
        "dots": {(0, 0): "red", (3, 0): "yellow"},
        "finish": "yellow",
        "goal": "Reach the yellow dot",
    },
    2: {
        "cols": 4, "rows": 3,
        "start": (0, 0),
        "dots": {(0, 0): "red", (3, 2): "yellow"},
        "finish": "yellow",
        "goal": "Reach the yellow dot",
    },
    3: {
        "cols": 5, "rows": 3,
        "start": (0, 0),
        "dots": {(2, 0): "blue", (4, 2): "green"},
        "finish": "green",
        "goal": "Visit blue, then reach green",
    },
    4: {
        "cols": 6, "rows": 4,
        "start": (0, 0),
        "dots": {(2, 0): "blue", (2, 3): "red", (5, 1): "green"},
        "finish": "green",
        "goal": "Visit blue, then red, then reach green",
    },
    5: {
        "cols": 7, "rows": 5,
        "start": (0, 2),
        "dots": {(3, 0): "blue", (6, 4): "red", (1, 4): "green"},
        "finish": "green",
        "goal": "Visit blue, then red, then reach green — try writing a function for each leg",
    },
    6: {
        "cols": 8, "rows": 5,
        "start": (0, 0),
        "dots": {(4, 0): "orange", (4, 4): "blue", (7, 2): "red", (7, 4): "green"},
        "finish": "green",
        "goal": "Visit orange, blue and red, then reach green",
    },
    7: {
        "cols": 6, "rows": 4,
        "start": (5, 2),
        "dots": {(1, 2): "blue", (1, 0): "green"},
        "finish": "green",
        "goal": "Visit blue then reach green — hint: moving right can wrap you to the other side",
    },
    8: {
        "cols": 9, "rows": 6,
        "start": (0, 0),
        "dots": {(3, 0): "blue", (8, 2): "orange", (5, 5): "purple", (0, 3): "green"},
        "finish": "green",
        "goal": "Visit blue, orange and purple, then reach green",
    },
    9: {
        "cols": 10, "rows": 7,
        "start": (0, 6),
        "dots": {(5, 6): "blue", (9, 3): "orange", (9, 0): "purple", (4, 0): "red", (0, 3): "green"},
        "finish": "green",
        "goal": "Visit blue, orange, purple and red, then reach green — write a function for each leg",
    },
    10: {
        "cols": 10, "rows": 8,
        "start": (0, 0),
        "dots": {(2, 7): "blue", (7, 7): "orange", (7, 3): "purple", (4, 1): "red", (9, 5): "green"},
        "finish": "green",
        "goal": "Visit blue, orange, purple and red, then reach green",
    },
    11: {
        "cols": 8, "rows": 8,
        "start": (0, 0),
        "dots": {
            (1, 1): "blue", (2, 2): "orange", (3, 3): "blue",
            (4, 4): "orange", (5, 5): "blue", (6, 6): "orange", (7, 7): "green",
        },
        "finish": "green",
        "goal": "Follow the diagonal — can you write a step() function and use a loop?",
    },
    12: {
        "cols": 9, "rows": 5,
        "start": (0, 0),
        "dots": {(2, 1): "blue", (4, 2): "orange", (6, 3): "purple", (8, 4): "green"},
        "finish": "green",
        "goal": "A chess knight moves 2 right and 1 up — write a knight() function and use a loop",
    },
    13: {
        "cols": 7, "rows": 3,
        "start": (0, 1),
        "dots": {(2, 1): "blue", (4, 1): "orange", (6, 1): "green"},
        "finish": "green",
        "goal": "Write a zigzag() function (right, up, right, down) and use a loop to collect each dot",
    },
    14: {
        "cols": 9, "rows": 7,
        "start": (0, 0),
        "dots": {(8, 0): "blue", (8, 6): "orange", (0, 6): "purple", (0, 3): "green"},
        "finish": "green",
        "goal": "Visit each corner of the rectangle — try writing a move_right_n(n) helper to keep each leg short",
    },
}

# ── extension: add your own challenges below ─────────────────────────────
#
# Each challenge needs:
#   "cols"   : number of columns
#   "rows"   : number of rows
#   "start"  : (col, row) where the cursor begins
#   "dots"   : {(col, row): "colour", ...}  — any named colour works
#   "finish" : the colour of the final dot to land on
#   "goal"   : a string describing the challenge
#
# Example:
# CHALLENGES[15] = {
#     "cols": 5, "rows": 5,
#     "start": (0, 0),
#     "dots": {(2, 2): "pink", (4, 4): "green"},
#     "finish": "green",
#     "goal": "Reach green via pink",
# }
