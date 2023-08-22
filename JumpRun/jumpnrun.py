
#-----------------------------------------------
# IMPORT LIBRARIES
#-----------------------------------------------

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
#import time
#from timer import timer, get_timer
from datetime import datetime
import math


#-----------------------------------------------
# BASE SETTINGS
#-----------------------------------------------

# window


# app
app = Ursina()
window.borderless = False
window.color = color.light_gray

# camera
camera.orthographic = True
camera.fov = 40

# ground
ground = Entity(model='cube', color=color.olive.tint(-.4), z=-.1, y=-1, origin_y=.7, scale=(1000,100,10), collider='box', ignore=True)

#floor = Entity(model='quad', y=-.5, origin_y=.5, collider='box', scale=(2,10), visible=True, color=color.azure)

#-----------------------------------------------
# ADD PLATFORMS
#-----------------------------------------------

Entity(model='cube'
        ,color=color.dark_gray
        ,collider='box'
        ,ignore=True
        ,position=(-7,-5)
        ,scale=(10,1,10)
)

Entity(model='cube'
        ,color=color.dark_gray
        ,collider='box'
        ,ignore=True
        ,position=(7,-5)
        ,scale=(10,1,10)
)




#-----------------------------------------------
# MAP INPUTS
#-----------------------------------------------

input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'space')
input_handler.bind('gamepad dpad right', 'd')
input_handler.bind('gamepad dpad left', 'a')
input_handler.bind('gamepad a', 'space')


#-----------------------------------------------
# ADD PLAYER
#-----------------------------------------------

# def input(key):
#     if key == 'c':
#         wall.collision = not wall.collision
#         print(wall.collision)

#player_controller = PlatformerController2d(scale_y=2, jump_height=4, x=3, y=20)
#camera.add_script(SmoothFollow(target=player_controller, offset=[0,1,-30], speed=4))

# variables
jumpbool = False # used to determine where the jump started
lastJumpX = 0   # last x position of the player before jumping
deadZoneY = -20 #camera.fov/2*-1 # y position where the player dies

# Text output
textx = Text(str(0), scale=2, font='VeraMono.ttf', resolution=100*Text.size, origin=(0,-4))
texty = Text(str(0), scale=2, font='VeraMono.ttf', resolution=100*Text.size, origin=(0,-3))
jump = Text(str(0), scale=2, font='VeraMono.ttf', resolution=100*Text.size, origin=(0,-6))

# Add simple player sprite
player = PlatformerController2d(scale_y=2
                                , jump_height=4
                                , x=3
                                , y=20
                                , max_jumps=2
                                )
def update():
        global jumpbool
        global lastJumpX
        global deadZoneY

        jump.text = str(round(player.y, 2))

        # we could also use the falling attribute of the player, when someone just falls down
        if player.jumping == True and jumpbool == False:
                lastJumpX = player.x
                textx.text = str(round(lastJumpX, 2))
                texty.text = str(round(player.y, 2))
                jumpbool = True
        
        # if we land, reset this variable
        if player.jumping == False and jumpbool == True:
                jumpbool = False

        # Player is dead -> respawn
        if player.y <= deadZoneY:
                player.x = lastJumpX
                player.y = camera.fov/2



# def update():
#     #t = datetime.now()
#     #second = t.second
#     textx.text = str(round(player.x, 2))
#     texty.text = str(round(player.y, 2))

camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))


# Respawn after falling down


# run
app.run()



