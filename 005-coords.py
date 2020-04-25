# coding: utf-8
"""Cartesian coordinates demo."""
import wasabi2d as w2d

scene = w2d.Scene()
scene.background = "#223366"

ylabel = scene.layers[0].add_label("0", pos=(10, 0))
xlabel = scene.layers[0].add_label("0", pos=(0, 25), align="center")

ax = scene.layers[0].add_line(
    [(5, 100), (5, 5), (100, 5)],
    color="white",
    stroke_width=2
)

centre = scene.width // 2, scene.height // 2
cursor = scene.layers[0].add_label(centre, pos=centre, align="center")


@w2d.event
def on_mouse_move(pos):
    global ax
    x, y = pos
    xlabel.x = xlabel.text = x
    ylabel.y = ylabel.text = y
    ax.vertices = [(5, y), (5, 5), (x, 5)]
    cursor.pos = cursor.text = pos


w2d.run()
