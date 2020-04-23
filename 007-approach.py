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


@w2d.event
def on_mouse_move(pos):
    actor.target = pos


LINEAR_SPEED = 10
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
funcs = cycle([approach_linear, approach_geometric])


@w2d.event
def on_mouse_down():
    global approach
    approach = next(funcs)


@w2d.event
def update():
    actor.pos = approach(actor.pos, actor.target)


w2d.run()
