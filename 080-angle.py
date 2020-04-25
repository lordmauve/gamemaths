"""Pythagoras's Theorem."""
import math
import wasabi2d as w2d
import numpy as np

scene = w2d.Scene()
scene.background = "#223366"

cx, cy = centre = scene.width // 2, scene.height // 2 - 30

scene.layers[0].add_circle(
    pos=centre,
    radius=200,
    color="yellow",
    fill=False,
    stroke_width=0.2,
)

alabel = scene.layers[0].add_label(0, pos=(cx, cy + 25), align="center")
blabel = scene.layers[0].add_label(0)
clabel = scene.layers[0].add_label('θ', align="center")

hypot = scene.layers[0].add_line(
    [centre, (0, 0)],
    color="white",
    stroke_width=2
)
ax = scene.layers[0].add_line(
    [centre, (0, centre[1]), (0, 0)],
    color="white",
    stroke_width=0.2
)

code = scene.layers[0].add_label(
    "vec = math.cos(theta), math.sin(theta)\n" +
    "theta = math.atan2(dy, dx)",
    pos=(50, 530),
    font="monospace",
)

vis = False


def build_arc(theta):
    points = abs(round(theta * 10))
    thetas = np.linspace(0, theta, points)
    xs = np.cos(thetas) * 20 + cx
    ys = np.sin(thetas) * 20 + cy
    return scene.layers[0].add_line(
        np.array([
            xs,
            ys,
        ]).T,
        stroke_width=1,
        color="white",
    )


arc = build_arc(90)


@w2d.event
def on_mouse_down(pos):
    global vis
    vis = not vis
    on_mouse_move(pos)


def normalize(dx, dy):
    """Normalize a vector."""
    mag = math.sqrt(dx * dx + dy * dy)
    if not mag:
        return 1, 0
    return dx / mag, dy / mag


@w2d.event
def on_mouse_move(pos):
    global ax, arc
    x, y = pos

    dx, dy = normalize(x - cx, y - cy)
    dx *= 200
    dy *= 200

    arc.delete()
    theta = math.atan2(dy, dx)
    if theta < 0:
        theta += 2 * math.pi
    arc = build_arc(theta)

    x, y = pos = cx + dx, cy + dy

    oy = math.copysign(20, dy)
    if dx > 0:
        blabel.align = 'left'
        blabel.pos = x + 10, cy + dy // 2
    else:
        blabel.align = 'right'
        blabel.pos = x - 10, cy + dy // 2

    if math.cos(theta / 2) > 0:
        clabel.align = 'left'
    else:
        clabel.align = 'right'

    clabel.pos = (
        cx + 30 * math.cos(theta / 2),
        cy + 40 * math.sin(theta / 2),
    )

    alabel.x = cx + dx // 2

    if vis:
        alabel.text = round(dx / 200, 3)
        blabel.text = round(dy / 200, 3)
        clabel.text = f'{theta / math.pi:0.2f}π'
    else:
        alabel.text = 'cos(θ)'
        blabel.text = 'sin(θ)'
        clabel.text = 'θ'

    ax.vertices = [centre, (x, centre[1]), pos]
    hypot.vertices = [centre, pos]


on_mouse_move(centre)
w2d.run()
