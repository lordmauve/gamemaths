import re
import wasabi2d as w2d
from wasabi2d import run
from wasabi2d.keyboard import keys
from collections import deque
from pathlib import Path
import types


scene = w2d.Scene(background="#223366")

slides = [
    p
    for p in Path(__file__).parent.iterdir()
    if re.match(r'^\d{3}', p.name)
]

slides = deque(sorted(slides, key=lambda p: p.name))


def show_slide(p):
    print("Showing", p)
    scene.layers.clear()
    w2d.clock.clock.clear()
    ns = types.ModuleType(p.name)
    exec(compile(p.read_text(), str(p), 'exec'), ns.__dict__)


def next_slide():
    slides.append(slides.popleft())
    show_slide(slides[0])


def prev_slide():
    slides.insert(0, slides.pop())
    show_slide(slides[0])


@w2d.event
def on_key_up(key):
    if key == keys.PAGEDOWN:
        next_slide()
    elif key == keys.PAGEUP:
        prev_slide()


show_slide(slides[0])

w2d.Scene = lambda **kwargs: scene
w2d.run = lambda: None
run()
