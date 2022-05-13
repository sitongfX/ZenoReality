# Welcome to Zeno_Reality's documentation!


## About

This is a fun action game made with python and ursina, an opensource game engine.


## Game Demo

[Check Out Trailer Here!](https://youtu.be/ThDYJI4Rjx4)

Trailer of your adventure in Zeno’s Reality.


## Artistic Vision (Very Abstract)

One of my favorite Zeno’s paradoxes is about the illusion of motion.
Achilles and the tortoise are in a race, in which the tortoise would start before Achilles, and it causes the latter to always fall behind. 

The reason of this is recounted by Aristotle in his *Physics VI*:9, 239b15:

> “In a race, the quickest runner can never over­take the slowest, since the pursuer must first reach the point whence the pursued started, so that the slower must always hold a lead.”
> 

Of course, in reality, this would never happen.

But I want to give Zeno a chance, to turn his paradox into reality, in the game I created. Thus, you the player will play the tortoise to outrun Achilles. The race is set on a glass bridge in the sky, so Achilles has to slow down to safely walk through the bridge. More, you are given the superpower to rewind the time and dash through the bridge without falling.

You will help prove that, some truths are mistaken as paradoxes (under extreme conditions).



## Game Instructions

There are two versions of the game. If you don’t have the hardware to make a game controller, you can play the keyboard version.

<aside>
with keyboard

- press C to change the color of the goal
- press M to mute
- press Q to elevate camera
- press A to lower camera
- use arrow keys to control the direction of the player
- use R to make the opponent retreat some random steps
- hold space to accelerate forward
</aside>

<aside>
with game controller

- use joystick to control the direction of the player
- use potentiometer to control the camera height
- press the button to make the opponent retreat, aka rewind the time.
- other unmentioned operations are same as the keyboard version.
</aside>


## Code

Go to [github!](https://github.com/sitongfX/ZenoReality/tree/main)


## API guide

For auto-generated api documentation, check pages under folder /autogen_api


## Guide for Building the Controller

### Materials Needed

- ESP32 TTGO T-display
- battery
- a button
- a joystick
- a potentiometer

### Detailed Step

1. Connect the wires
    1.can use female-to-female wires or solderless breadboard instead of soldering the wires for convenience
    2. for button, connect to pin 15 and ground on TTGO T-display
    3. for potentiometer’s 3 pins, connect to bottom left 3.3V, pin 12, and ground correspondingly

    4. for joystick, the connection should be as follows:
        
        - Joystick GND -> bottom right ground on the TTGO	
        
        - Joystick 5V -> top right 3V
        
        - Joystick VRy -> TTGO 27
        
        - Joystick VRx -> TTGO 26
        
        - Joystick SW  -> TTGO 25
        
2. Build enclosures
    1. use durable material to enclose every hardware piece inside
    2. design appropriate layout that is suitable for human natural posture
3. Download the code
    1. upload the code to the ESP32
    2. check the serial message in json (using serial monitor from Arduino IDE)
    3. fix the code to make sure it works properly on your computer
4. Begin the journey to Zeno’s reality


```eval_rst
.. note::
   Be mindful of the serial data transmission between your devices. When using joystick, wait patiently for actions to synchronize between devices.
```

