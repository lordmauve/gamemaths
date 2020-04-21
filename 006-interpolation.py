"""Illustrate interpolation with different easing functions."""
import wasabi2d as w2d
import numpy as np
from itertools import cycle


scene = w2d.Scene(background="#223366")

scene.layers[0].add_line(
    [(100, 100), (100, 500), (500, 500)],
    color='#cccccc',
)

TIMES = np.linspace(0, 1, 200)
ys = TIMES

plot = scene.layers[0].add_line(
    np.array([
        TIMES * 400 + 100,
        500 - ys * 400
    ]).T,
    color='yellow',
    stroke_width=2
)

mark = scene.layers[1].add_circle(
    pos=(100, 500),
    radius=8,
    color='red',
)


TOP = 100
BOTTOM = 500

actor = scene.layers[1].add_circle(
    pos=(700, TOP),
    radius=30,
    color='green'
)


async def move_actor():
    for target in cycle([BOTTOM, TOP]):
        sy = actor.y
        async for t in w2d.clock.coro.frames(seconds=1):
            frac = np.interp(t, TIMES, ys)
            actor.y = target * frac + (1 - frac) * sy

            mark.pos = 100 + t * 400, 500 - 400 * frac


        await w2d.clock.coro.sleep(1)


functions = cycle([
    lambda x: x ** 2,
    lambda x: x ** 0.5,
    lambda x: 0.5 - 0.5 * np.cos(np.pi * x),
    lambda x: x,
])


async def switch_interp(func):
    global ys
    new_ys = func(TIMES)
    orig_ys = ys

    async for t in w2d.clock.coro.frames(seconds=0.2):
        frac = t / 0.2
        ys = frac * new_ys + (1 - frac) * ys
        plot.vertices = np.array([
            TIMES * 400 + 100,
            500 - ys * 400
        ]).T



@w2d.event
def on_mouse_down():
    w2d.clock.coro.run(switch_interp(next(functions)))


w2d.clock.coro.run(move_actor())

w2d.run()
