# ZenoReality

![GitHub](https://img.shields.io/github/license/sitongfX/ZenoReality)
[![CI](https://github.com/sitongfX/ZenoReality/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/sitongfX/ZenoReality/actions/workflows/main.yml)
[![codecov](https://codecov.io/gh/sitongfX/ZenoReality/branch/main/graph/badge.svg?token=5CVVR0707X)](https://codecov.io/gh/sitongfX/ZenoReality)
![Read the Docs](https://img.shields.io/readthedocs/zenoreality)

## What is it
The project uses a interactive controller to journey into a philosophical game with absolute freedom. See detailed [ducumentation](https://zenoreality.readthedocs.io/en/stable/) page for hardware building and playing instructions. The game uses [ursina](https://www.ursinaengine.org/), an open source game engine and Python.

A prettier read-me is [here](https://sitongfx.github.io/ZenoReality/) too.


## Demo Picture
Game Scene: 
**click image to see a demo trailler**
[![game](game.png)](https://youtu.be/ThDYJI4Rjx4)
click image to see a demo trailler

Controller:
![controller](controller.jpg)

## API Guide

Sample auto-generated api documentation:
<img width="694" alt="api" src="https://user-images.githubusercontent.com/71209023/168211575-d28cdf47-2f16-4054-be63-fb71de95396e.png">

more api pages under folder [/autogen_api](https://github.com/sitongfX/ZenoReality/tree/main/autogen_api)


Prerequite:
1. Make sure ursina engine is downloaded.
2. Have Python 3.6 or newer.

Use the following command to run the program under the project path:

``` bash
# install ursina in terminal
pip install ursina
```

Then run the game with the appropriate version

``` bash
python keyboard_game.py     # if you are playing with keyboard
```
or

``` bash
python controller_game.py # if you are playing with a controller
```
make sure to check out the hardware guide in the detailed documentation mentioned above.

