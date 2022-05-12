from tkinter import Button
from turtle import color
from random import randint

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from connecting_serial_controller import connect_ser

# two parts
# 1. get message from json manually

# functions:
# potentiometer = camera height
# joystick = direction of the player
# button = rewind the time

ser = connect_ser()

# 2. the game


while True:

    app = Ursina()

    player = FirstPersonController(collider="box", speed=5, scale=2, max_jumps=2)
    B = Button(scale=0.1, icon="sword", position=(0.65, 0.4))
    B.on_click = B.fade_out(duration=0.5)

    ground = Entity(model="plane", texture="grass", collider="mesh", scale=(30, 0, 3))

    bridge1 = Entity(model="cube", texture="brick", scale=(0.4, 0.1, 53), z=28, x=-0.7)

    bridge2 = duplicate(bridge1, x=-3.7)
    bridge3 = duplicate(bridge1, x=0.6)
    bridge4 = duplicate(bridge1, x=3.6)

    blocks = []
    for i in range(12):
        block = Entity(
            model="cube",
            collider="box",
            color=color.white33,
            position=(2, 0.1, 3 + i * 4),
            scale=(3, 0.1, 2.5),
        )
        block2 = duplicate(block, x=-2.2)

        blocks.append((block, block2, randint(0, 3) > 0, randint(0, 3) > 0))

    goal = Entity(
        color=color.brown, model="cube", collider="box", scale=(10, 1, 10), z=55
    )

    goal_animate = Sequence(
        1, Func(goal.blink, duration=5), Func(goal.shake, duration=15), Loop=True
    )
    goal_animate.start()

    # audio
    a = Audio("yamato", pitch=1, loop=True, autoplay=True)
    a.volume = 20

    def input(key):
        if key == "m":
            a.volume = 0
        if key == "c":
            goal.color = color.rgb(randint(0, 255), randint(0, 255), randint(0, 255))

    def update():

        try:
            con = []  # list of values from controllers: P, X, Y, B
            data = str(ser.readline().strip())[3:-2]
            items = data.split(",")
            for i in items:
                temp = i.split(":")
                con.append(int(temp[1]))
            # print(con)

            if len(con) == 4:  # make sure data is not corrupted

                camera.position = (0, time.dt * con[0], 0)

                if con[1] > 75:  # joy stick X
                    move_right = True
                elif con[1] < 25:
                    move_left = True
                else:
                    move_right = False
                    move_left = False

                if con[2] > 75:  # joy stick Y
                    move_forward = True
                elif con[2] < 25:
                    move_back = True
                else:
                    move_forward = False
                    move_back = False

                if move_right:
                    player.x += time.dt * player.speed  # go right

                if move_left:
                    player.x -= time.dt * player.speed  # go left

                if move_forward:
                    player.z += time.dt * player.speed  # go forward

                if move_back:
                    player.z -= time.dt * player.speed  # go backward

                if held_keys["space"]:
                    player.z += time.dt * player.speed * 2.5  # dash forward

                if con[3]:
                    rewind_dis = randint(0, 100) * 0.1
                    if rewind_dis > firstMan.z:
                        while firstMan.z > 0:
                            firstMan.z -= 0.05
                    else:
                        firstMan.z = firstMan.z - rewind_dis
                    if rewind_dis > player.z:
                        while player.z > 0:
                            player.z -= 0.01
                    else:
                        player.z = player.z - rewind_dis

                firstMan.z = firstMan.z + time.dt * 2.05

                if player.y < -5:
                    Text(
                        text="You died for a great cause!",
                        origin=(0, 0),
                        scale=2,
                        color=color.orange,
                    )

        except Exception:
            pass

    class Man(FrameAnimation3d):
        def __init__(self):
            super().__init__(
                "walking_",
                fps=100,
                frame_times=138,
                autoplay=True,
                loop=True,
                scale=4,
                position=(-2, 0.5, -5),
                texture="Uriel_diffuse",
            )

    firstMan = Man()
    window.title = "Zeno's reality"
    Sky(texture="sky_sunset", rotation=(0, 90, 0))
    scene.fog_density = 0.1  # sets exponential density
    scene.fog_density = (50, 200)
    app.run()
