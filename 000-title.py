"""Title screen."""
import wasabi2d as w2d

scene = w2d.Scene(background="#223366")

cx, cy = scene.width // 2, scene.height // 2

title = scene.layers[0].add_label(
    "Game maths in 10 minutes",
    pos=(cx, -10),
    font='comfortaa',
    fontsize=48,
    align='center',
)
subtitle = scene.layers[0].add_label(
    "Daniel Pope     @lordmauve",
    pos=(cx, -10),
    font='comfortaa',
    fontsize=30,
    align='center',
)


async def animate_title():
    w2d.animate(title, tween='bounce_end', y=cy - 80)
    await w2d.clock.coro.sleep(1 / 2.75)
    w2d.animate(title, tween='decelerate', duration=0.1, angle=0.1)
    await w2d.clock.coro.sleep(0.2)
    w2d.animate(subtitle, tween='bounce_end', y=cy + 200)


@w2d.event
def on_mouse_down():
    w2d.clock.coro.run(animate_title())

w2d.run()
