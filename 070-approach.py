"""Illustrate interpolation with different easing functions."""
import wasabi2d as w2d
import numpy as np
from itertools import cycle


scene = w2d.Scene(background="#223366")

actor = scene.layers[1].add_star(
    points=6,
    outer_radius=30,
    inner_radius=20,
    pos=(0, 0),
    color='cyan'
)
actor.target = 400, 400


scene.layers[0].add_line(
    [(50, 450), (50, 550), (750, 550)],
    color='#cccccc',
)

TIMES = np.linspace(0, 1, 50)
plot = scene.layers[0].add_line(
    np.zeros((len(TIMES), 2)),
    color='yellow',
    stroke_width=2
)


func_label = scene.layers[0].add_label(
    "pos += SPEED * normalize(target - pos)",
    pos=(750, 475),
    align="right",
    font="monospace",
)


@w2d.event
def on_mouse_move(pos):
    actor.target = pos


LINEAR_SPEED = 8
APPROACH_PER_FRAME = 0.1


def normalize(dx, dy):
    """Normalize a vector."""
    mag = np.sqrt(dx * dx + dy * dy)
    if not mag:
        return 1, 0
    return dx / mag, dy / mag


def approach_linear(pos, target):
    x, y = pos
    tx, ty = target

    nx, ny = normalize(tx - x, ty - y)
    x += nx * LINEAR_SPEED
    y += ny * LINEAR_SPEED

    return x, y


def approach_geometric(pos, target):
    x, y = pos
    tx, ty = target

    x += (tx - x) * APPROACH_PER_FRAME
    y += (ty - y) * APPROACH_PER_FRAME

    return x, y


approach = approach_linear
funcs = cycle([
    ("pos += SPEED * normalize(target - pos)", approach_linear),
    ("pos += (target - pos) * RATE  # rate in (0, 1)", approach_geometric),
])



def plot_approach(func):
    ys = []
    pos = (100, 0)
    target = (0, 0)
    for v in TIMES:
        ys.append(pos[0])
        pos = func(pos, target)
    return np.array([
        TIMES * 700 + 50,
        550 - np.array(ys)
    ]).T


plot.vertices = plot_approach(approach)



@w2d.event
def on_mouse_down():
    global approach
    label, approach = next(funcs)
    plot.vertices = plot_approach(approach)
    func_label.text = label


@w2d.event
def update():
    actor.pos = approach(actor.pos, actor.target)


w2d.run()
