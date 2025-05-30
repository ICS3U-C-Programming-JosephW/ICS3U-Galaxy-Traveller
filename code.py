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

# Import the constants file
# for useful constants.
import constants


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
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Create a ship sprite by selecting the sixth
    # image off the sprite image bank (0 index). Set
    # its position to 75 in the x and double its size
    # away from the bottom of the screen in the y.
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # Refresh the display at a 60 Hz frequency (60 FPS).
    game = stage.Stage(ugame.display, constants.FPS)

    # Set the layers with ordered items.
    game.layers = [ship] + [background]

    # Render the layers onto the screen.
    game.render_block()

    # Construct an infinite loop.
    while True:
        # Get the user input from the
        # current buttons they are pressing.
        keys = ugame.buttons.get_pressed()

        # Check if the user pressed the
        # 'A' button on the PyBadge.
        if keys & ugame.K_X:
            # Do nothing by using pass
            # as a placeholder for now.
            pass
        # Check if the user pressed the
        # 'B' button on the PyBadge.
        if keys & ugame.K_O:
            # Do nothing by using pass
            # as a placeholder for now.
            pass
        # Check if the user pressed the
        # 'Start' button on the PyBadge.
        if keys & ugame.K_START:
            # Do nothing by using pass
            # as a placeholder for now.
            pass
        # Check if the user pressed the
        # 'Select' button on the PyBadge.
        if keys & ugame.K_SELECT:
            # Do nothing by using pass
            # as a placeholder for now.
            pass
        # Check if the user pressed the
        # keypad right button on the PyBadge.
        if keys & ugame.K_RIGHT:
            # Check if the x-coordinate of the
            # ship is within the length of the
            # screen, meaning on the screen.
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                # Move the ship by its movement speed right from the origin.
                ship.move(ship.x + constants.SPRITE_MOVEMENT_SPEED, ship.y)
            # Otherwise, the ship is not on the
            # screen and it is out of the screen
            # length.
            else:
                # Reset the position of the ship
                # to the right edge of the screen,
                # and subtract it by the sprite size.
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        # Check if the user pressed the
        # keypad left button on the PyBadge.
        if keys & ugame.K_LEFT:
            # Check if the ship is in the
            # positive x range or zero,
            # meaning on the screen.
            if ship.x >= 0:
                # Move the ship by its movement speed left from the origin.
                ship.move(ship.x - constants.SPRITE_MOVEMENT_SPEED, ship.y)
            # Otherwise, it is not on the screen
            # and the x-coordinate of the ship is
            # negative.
            else:
                # Reset the position of the ship
                # to zero, keeping it on the left
                # edge of the screen.
                ship.move(0, ship.y)
        # Check if the user pressed the
        # keypad up button on the PyBadge.
        if keys & ugame.K_UP:
            # Do nothing by using pass
            # as a placeholder for now.
            pass
        # Check if the user pressed the
        # keypad down button on the PyBadge.
        if keys & ugame.K_DOWN:
            # Do nothing by using pass
            # as a placeholder for now.
            pass

        # Redraw the sprites, with
        # only the ship for now.
        game.render_sprites([ship])

        # Wait for the 1/60th of a second
        # to occur for the accurate refresh
        # rate, dependent on frequency.
        game.tick()


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the main game scene function if so.
    game_scene()
