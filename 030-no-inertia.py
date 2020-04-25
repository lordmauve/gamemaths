# coding: utf-8
"""Control a sprite without inertia."""
import wasabi2d as w2d

scene = w2d.Scene()
scene.background = "#223366"

centre = scene.width // 2, scene.height // 2
blob = scene.layers[0].add_sprite('blob', pos=centre)

equation = scene.layers[0].add_label(
    "position += SPEED * input",
    pos=(centre[0], scene.height - 60),
    align="center",
    font="monospace",
)

SPEED = 5


@w2d.event
def update(keyboard):
    if keyboard.left:
        blob.x -= SPEED
    elif keyboard.right:
        blob.x += SPEED

    if keyboard.up:
        blob.y -= SPEED
    elif keyboard.down:
        blob.y += SPEED


w2d.run()
