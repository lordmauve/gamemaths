# coding: utf-8
"""Illustrate interpolation with different easing functions."""
import wasabi2d as w2d
import numpy as np
from itertools import cycle


scene = w2d.Scene(background="#223366")

scene.layers[0].add_line(
    [(50, 100), (50, 500), (450, 500)],
    color='#cccccc',
)

TIMES = np.linspace(0, 1, 200)
ys = TIMES

plot = scene.layers[0].add_line(
    np.array([
        TIMES * 400 + 50,
        500 - ys * 400
    ]).T,
    color='yellow',
    stroke_width=2
)

def label(text, pos, align="right", font=None):
    return scene.layers[0].add_label(
        text,
        pos=pos,
        align=align,
        font=font,
    )


label('pos = A + f(t / end) * (B - A)', (790, 525), "right", font="monospace")

label('1', (45, 105))
label('0', (45, 505))
label('1', (450, 520))
label('t', (350, 540))


func_label = label('f(t) = t', (450, 80), font="monospace")

mark = scene.layers[1].add_circle(
    pos=(50, 500),
    radius=8,
    color='red',
)


TOP = 100
BOTTOM = 450

actor = scene.layers[1].add_circle(
    pos=(630, TOP),
    radius=30,
    color='green'
)


async def move_actor():
    for target in cycle([BOTTOM, TOP]):
        sy = actor.y
        async for t in w2d.clock.coro.frames(seconds=1):
            frac = np.interp(t, TIMES, ys)
            actor.y = target * frac + (1 - frac) * sy

            mark.pos = 50 + t * 400, 500 - 400 * frac


        await w2d.clock.coro.sleep(1)


functions = cycle([
    ('f(t) = t * t', TIMES ** 2),
    ('f(t) = 2 * t - t * t', 2 * TIMES - TIMES ** 2),
    (
        'f(t) = (1 - math.cos(t * math.pi)) / 2',
        0.5 - 0.5 * np.cos(np.pi * TIMES)
    ),
    ('f(t) = <4 parabolas>',
        np.array(list(map(w2d.animation.bounce_end, TIMES)))
    ),
    ('f(t) = t', TIMES),
])


async def switch_interp(new_ys):
    global ys
    orig_ys = ys

    async for t in w2d.clock.coro.frames(seconds=0.2):
        frac = t / 0.2
        ys = frac * new_ys + (1 - frac) * ys
        plot.vertices = np.array([
            TIMES * 400 + 50,
            500 - ys * 400
        ]).T



@w2d.event
def on_mouse_down():
    newtext, newfunc = next(functions)
    func_label.text = newtext
    w2d.clock.coro.run(switch_interp(newfunc))


w2d.clock.coro.run(move_actor())

w2d.run()
