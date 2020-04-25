# coding: utf-8
"""Control a sprite without inertia."""
import wasabi2d as w2d

scene = w2d.Scene(background="#223366")

centre = scene.width // 2, scene.height // 2

blob = scene.layers[0].add_sprite('blob-happy', pos=centre)
blob.vx = blob.vy = 0

equation = scene.layers[0].add_label(
    "velocity = input * ACCEL + velocity * DRAG\n" +
    "position += velocity",
    pos=(centre[0], scene.height - 60),
    align="center",
    font="monospace",
)

ACCEL = 1
DRAG = 0.85


@w2d.event
def update(keyboard):
    blob.vx *= DRAG
    blob.vy *= DRAG

    if keyboard.left:
        blob.vx -= ACCEL
    elif keyboard.right:
        blob.vx += ACCEL

    if keyboard.up:
        blob.vy -= ACCEL
    elif keyboard.down:
        blob.vy += ACCEL

    blob.x += blob.vx
    blob.y += blob.vy


w2d.run()
