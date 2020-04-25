# coding: utf-8
"""Pythagoras's Theorem."""
import math
import wasabi2d as w2d

scene = w2d.Scene()
scene.background = "#223366"

GREEN = '#00aa00'
RED = '#cc0000'

cx, cy = centre = scene.width // 2, scene.height // 2

alabel = scene.layers[0].add_label(0, pos=(cx, cy + 25), align="center")
blabel = scene.layers[0].add_label(0)


equation = scene.layers[0].add_label(
    0,
    pos=(cx, scene.height - 40),
    align="center"
)

circle1 = scene.layers[-1].add_circle(
    pos=centre,
    radius=58,
    color='yellow',
    fill=False,
    stroke_width=2,
)
circle2 = scene.layers[-1].add_circle(
    pos=centre,
    radius=98,
    color=GREEN,
    fill=False,
    stroke_width=2,
)

hypot = scene.layers[0].add_line(
    [centre, (0, 0)],
    color="white",
    stroke_width=1
)
ax = scene.layers[0].add_line(
    [centre, (0, centre[1]), (0, 0)],
    color="white",
    stroke_width=0.2
)


vis = False


@w2d.event
def on_mouse_down(pos):
    global vis
    vis = not vis
    on_mouse_move(pos)


def p(v):
    if v < 0:
        return f'({v})'
    return str(v)


@w2d.event
def on_mouse_move(pos):
    global ax
    x, y = pos

    dx = x - cx
    dy = y - cy

    circle2.pos = pos

    oy = math.copysign(20, dy)
    if dx > 0:
        blabel.align = 'left'
        blabel.pos = x + 10, cy + dy // 2
    else:
        blabel.align = 'right'
        blabel.pos = x - 10, cy + dy // 2
    alabel.x = cx + dx // 2

    alabel.text = dx
    blabel.text = dy

    # Collision test
    collision = (dx * dx + dy * dy) < 160 * 160

    eq = '<' if collision else '>'

    if vis:
        equation.text = f'{p(dx)}² + {p(dy)}² {eq} {160 * 160}'
    else:
        equation.text = f'dx² + dy² {eq} (ra + rb)²'

    circle2.color = RED if collision else GREEN

    ax.vertices = [centre, (x, centre[1]), pos]
    hypot.vertices = [centre, pos]


on_mouse_move(centre)
w2d.run()
