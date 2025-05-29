#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 26, 2025
# This main file is for the Space
# Aliens program on the PyBadge.

# Import the ugame module for
# managing sounds and controls.
# import ugame

# Import the stage module for
# screen display functions.
# import stage


# Define the main game scene function to run the whole game.
def game_scene():
    # Get an image bank from a 16-bit bitmap
    # to use a background bank for the game.
    # image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # Set the background to image 0 of the background bank
    # with a 10x8 grid on the PyBadge display, representing
    # its full size of 16x16 images it can contain.
    # background = stage.Grid(image_bank_background, 10, 8)

    # Construct an infinite loop.
    while True:
        # Do nothing by using pass as a placeholder for now.
        pass


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main game scene function if so.
    game_scene()
