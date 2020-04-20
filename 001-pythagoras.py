"""Pythagoras's Theorem."""
import math
import wasabi2d as w2d

scene = w2d.Scene()
scene.background = "#223366"

cx, cy = centre = scene.width // 2, scene.height // 2

alabel = scene.layers[0].add_label(0, pos=(cx, cy + 25))
blabel = scene.layers[0].add_label(0)
clabel = scene.layers[0].add_label(0)

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

vis = False


@w2d.event
def on_mouse_down(pos):
    global vis
    vis = not vis
    on_mouse_move(pos)


@w2d.event
def on_mouse_move(pos):
    global ax
    x, y = pos

    dx = x - cx
    dy = y - cy

    oy = math.copysign(20, dy)
    if dx > 0:
        blabel.align = 'left'
        clabel.align = 'right'
        blabel.pos = x + 10, cy + dy // 2
        clabel.pos = cx + dx // 2, cy + dy // 2 + oy
    else:
        blabel.align = 'right'
        clabel.align = 'left'
        blabel.pos = x - 10, cy + dy // 2
        clabel.pos = cx + dx // 2, cy + dy // 2 + oy

    alabel.x = cx + dx // 2

    if vis:
        alabel.text = dx
        blabel.text = dy
        clabel.text = '{:0.2f}'.format(math.hypot(dx, dy))
    else:
        alabel.text, blabel.text = 'ab'
        clabel.text = 'a² + b²'

    ax.vertices = [centre, (x, centre[1]), pos]
    hypot.vertices = [centre, pos]


on_mouse_move(centre)
w2d.run()
