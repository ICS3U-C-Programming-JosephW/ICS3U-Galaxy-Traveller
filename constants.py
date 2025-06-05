#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 30, 2025
# This module contains constants.


# Set a constant for the screen length.
SCREEN_X = 160
# Set a constant for the screen width.
SCREEN_Y = 128
# Set a constant for the amount of grids lengthwise.
SCREEN_GRID_X = 10
# Set a constant for the amount of grids widthwise.
SCREEN_GRID_Y = 8
# Set a constant for the sprite size in pixels.
SPRITE_SIZE = 16
# Set a constant for the total number of aliens.
TOTAL_NUMBER_OF_ALIENS = 5
# Set a constant for the total number of lasers.
TOTAL_NUMBER_OF_LASERS = 5
# Set a constant for the ship speed in pixels.
SHIP_SPEED = 1
# Set a constant for the alien speed in pixels.
ALIEN_SPEED = 1
# Set a constant for the laser speed in pixels.
LASER_SPEED = 2
# Set a constant for the off
# screen laser position in the x.
OFF_SCREEN_X = -100
# Set a constant for the off
# screen laser position in the y.
OFF_SCREEN_Y = -100
# Set a constant for the negative sprite size
# to get itself off the top of the screen.
OFF_TOP_SCREEN = -1 * SPRITE_SIZE
# Set a constant for the resulting
# position needed to get the sprite
# off the bottom of the screen.
OFF_BOTTOM_SCREEN = SCREEN_Y + SPRITE_SIZE
# Set a constant for the frames per second (frequency).
FPS = 60
# Set a constant for the movement speed of the sprite in pixels.
SPRITE_MOVEMENT_SPEED = 1


# Set a constant dictionary to hold the possible button states.
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released",
}


# Set a constant to hold the hexadecimal
# arrangement for a red palette.
RED_PALETTE = (
    b"\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)

# Set a constant to hold the hexadecimal
# arrangement for a blue palette.
BLUE_PALETTE = (
    b"\xf8\x1f\x00\x00\xcey\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
)
