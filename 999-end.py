"""Title screen."""
import wasabi2d as w2d

scene = w2d.Scene(background="#223366")

cx, cy = scene.width // 2, scene.height // 2

slides_link = scene.layers[0].add_label(
"""\
github.com/lordmauve/gamemaths

wasabi2d.readthedocs.io

pyweek.org
""",
    pos=(cx, cy - 150),
    font='comfortaa',
    fontsize=30,
    align='center',
    color='cyan'
)

logo = scene.layers[0].add_sprite(
    "wasabi2d",
    pos=(cx, scene.height - 100),
    scale=0.7
)


effect = scene.layers[0].set_effect('punch')
effect.factor = 1


async def bounce():
    while True:
        await w2d.animate(effect, duration=0.1, factor=1.5)
        await w2d.animate(effect, 'bounce_end', factor=1)
        await w2d.clock.coro.sleep(3)


w2d.clock.coro.run(bounce())
w2d.run()
