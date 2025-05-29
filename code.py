#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: May 26, 2025
# This main file is for the Space
# Aliens program on the PyBadge.

# Import the ugame module for
# managing sounds and controls.
import ugame

# Import the stage module for
# screen display functions.
import stage


# Define the main game scene function to run the whole game.
def game_scene():
    # Import a 16-bit bitmap image which contains
    # the background image bank for the game.
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Import another 16-bit bitmap image
    # containing the game sprites.
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Create a grid of the image background with a
    # 10x8 tile grid on the PyBadge display, representing
    # its full size of 16x16 images it can contain.
    background = stage.Grid(image_bank_background, 10, 8)

    # Create a ship sprite by selecting the fifth
    # image off the sprite image bank. Set its
    # position to 75 in the x and 66 in the y
    # from the origin.
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    # Refresh the display at a 60 Hz frequency (60 FPS).
    game = stage.Stage(ugame.display, 60)

    # Set the layers with ordered items.
    game.layers = [ship] + [background]

    # Render the layers onto the screen.
    game.render_block()

    # Construct an infinite loop.
    while True:
        # Redraw the sprites, with
        # only the ship for now.
        game.render_sprites([ship])

        # Wait for the 1/60th of a second
        # to occur for the accurate refresh
        # rate, dependent on frequency.
        game.tick()

        # Handle movement later.


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main game scene function if so.
    game_scene()
