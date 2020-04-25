"""Control a sprite without inertia."""
import wasabi2d as w2d
from wasabi2d.keyboard import keyboard, keys

scene = w2d.Scene(background="#223366")

centre = scene.width // 2, scene.height // 2

blob = scene.layers[0].add_sprite('blob-happy', pos=centre)
blob.vx = blob.vy = 0

equation = scene.layers[0].add_label(
    "v_initial = velocity\n" +
    "velocity = input * ACCEL * dt + velocity * DRAG ** dt\n" +
    "position += 0.5 * (v_initial + velocity) * t",
    pos=(centre[0], scene.height - 80),
    align="center",
    font="monospace",
)

speedlabel = scene.layers[0].add_label(
    "Slow-down: 1",
    pos=(10, 30),
)


ACCEL = 1
DRAG = 0.85

dt = 1
FPS = 60


def update():
    ux, uy = blob.vx, blob.vy

    blob.vx *= DRAG ** dt
    blob.vy *= DRAG ** dt

    if keyboard.left:
        blob.vx -= ACCEL * dt
    elif keyboard.right:
        blob.vx += ACCEL * dt

    if keyboard.up:
        blob.vy -= ACCEL * dt
    elif keyboard.down:
        blob.vy += ACCEL * dt

    blob.x += 0.5 * (ux + blob.vx) * dt
    blob.y += 0.5 * (uy + blob.vy) * dt


@w2d.event
def on_key_down(key):
    global dt
    if key == keys.EQUALS:
        dt = min(dt + 1, 6)
    elif key == keys.MINUS:
        dt = max(dt - 1, 1)
    else:
        return

    speedlabel.text = f"Slow-down: {dt}"

    w2d.clock.unschedule(update)
    w2d.clock.schedule_interval(update, dt / FPS)

w2d.clock.schedule_interval(update, dt / FPS)
w2d.run()
