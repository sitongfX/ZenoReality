from tkinter import Button
from turtle import color
from random import randint

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


def audio_adjust(key_input):
    if key_input == 'm':
        a.volume = 0
        return True

def color_adjust(key_input):
    if key_input == 'c':
        goal.color = color.rgb(randint(0,255), randint(0,255),randint(0,255))
        return True

def input(key):
    audio_adjust(key)
    color_adjust(key)

def update():

  if held_keys['q']:                             # If q is pressed
    camera.position += (0, 0.5*time.dt, 0)           # move up vertically
  if held_keys['a']:                             # If a is pressed
    camera.position -= (0, time.dt, 0)           # move down vertically

  player.x += held_keys['right arrow'] * time.dt * player.speed  # go right
  
  player.x -= held_keys['left arrow'] * time.dt * player.speed   # go left

  player.z += held_keys['up arrow'] * time.dt * player.speed     # go forward
  
  player.z -= held_keys['down arrow'] * time.dt * player.speed   # go backward

  player.z += held_keys['space'] * time.dt * player.speed * 2.5  # dash forward

  firstMan.z = firstMan.z + time.dt*2.05

  # if firstMan.z > player.z:
  #    Text(text="You are a loser!", origin=(0,0), scale=2)
  if player.y < -5:
    Text(text="You died for a great cause!", origin=(0,0), scale=2, color = color.orange)  

  if held_keys['r']:
      rewind_dis = (randint(0,100)*0.1)
      if rewind_dis > firstMan.z:
        while firstMan.z > 0:
          firstMan.z -= 0.05
      else:
        firstMan.z = firstMan.z - rewind_dis
      # if rewind_dis > player.z:
      #     while player.z > 0:
      #       player.z -= 0.01
      # else:
      #   player.z = player.z - rewind_dis

app  =  Ursina()

player  =  FirstPersonController(
  collider = 'box',
  speed = 5,
  scale = 2,
  max_jumps=2
)
B = Button(scale=0.1, icon="sword", position = (0.65, 0.4))
B.on_click = B.fade_out(duration=0.5)

ground  =  Entity(
  model = 'plane',
  texture = 'grass',
  collider = 'mesh',
  scale = (30,0,3)
)

bridge1  =  Entity(
  model = 'cube',
  # color = color.violet,
  texture = 'brick',
  scale = (0.4,0.1,53),
  z = 28,x = -0.7
)

bridge2 = duplicate(bridge1, x = -3.7)
bridge3 = duplicate(bridge1, x = 0.6)
bridge4 = duplicate(bridge1, x = 3.6)

blocks = []
for i in range(12):
  block = Entity(
    model = 'cube', 
    collider = 'box',
    color = color.white33,
    position = (2,0.1,3+i*4),
    scale = (3,0.1,2.5)
  )
  block2 = duplicate(block, x = -2.2)

  blocks.append(
    (block, block2, randint(0,3)>0,randint(0,3)>0)
  )

goal = Entity(
  color = color.brown,
  collider = 'box',
  model='cube',
  scale=(10,1,10), 
  z=55
)


goal_animate = Sequence(1, Func(goal.blink, duration = 5), Func(goal.shake, duration=15), Loop = True)
goal_animate.start()


a = Audio('yamato', pitch=1, loop=True, autoplay=True)
a.volume = 20

class Man(FrameAnimation3d):
  def __init__(self):
      super().__init__(
        "walking_",
        fps = 100,
        frame_times = 138,
        autoplay = True,
        loop = True,
        scale = 4,
        position = (-2,0.5,-5),
        texture = "Uriel_diffuse"
      )  

firstMan = Man()
window.title = "Zeno's reality"
Sky(texture = "sky_sunset", rotation = (0,90,0))
scene.fog_density = .1          # sets exponential density
scene.fog_density = (50, 200) 
app.run()




