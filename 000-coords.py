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


@w2d.event
def on_mouse_move(pos):
    global ax
    x, y = pos
    xlabel.x = x
    xlabel.text = str(x)
    ylabel.y = y
    ylabel.text = str(y)
    ax.delete()
    ax = scene.layers[0].add_line(
        [(5, y + 5), (5, y), (5, 5), (x, 5), (x + 5, 5)],
        color="white",
        stroke_width=2
    )


w2d.run()
