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

# Import the time module for
# time-related functions.
import time

# Import the random module for
# random number generators.
import random

# Import the supervisor module
# for handling game relaunching.
import supervisor

# Import the constants file
# for useful constants.
import constants


# Define the splash scene function to introduce the starting menu.
def splash_scene():
    # Initialize the 'coin' sound by opening its
    # wave file. Use 'rb' to correctly handle
    # the audio file by reading it in binary.
    coin_sound = open("coin.wav", "rb")
    # Access the game's audio.
    sound = ugame.audio
    # Stop all sounds from playing
    # to avoid unusual sound states.
    sound.stop()
    # Enable the sound, if not activated already.
    sound.mute(False)
    # Play the initial coin sound
    # for the splash scene.
    sound.play(coin_sound)

    # Import a 16-bit bitmap image which contains
    # the background image bank for the menu.
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a grid of the menu background with a
    # 10x8 tile grid on the PyBadge display, representing
    # its full size of 16x16 images it can contain.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Used this program to split the light bulb image into tiles:
    # https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    # Manually set the first recurring
    # column of tiles and their locations.
    background.tile(2, 2, 0)
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)

    # Manually set the second recurring
    # column of tiles and their locations.
    background.tile(2, 3, 0)
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)

    # Manually set the third recurring
    # column of tiles and their locations.
    background.tile(2, 4, 0)
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)

    # Manually set the fourth recurring
    # column of tiles and their locations.
    background.tile(2, 5, 0)
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)

    # Refresh the display at a 60 Hz frequency (60 FPS).
    game = stage.Stage(ugame.display, constants.FPS)

    # Set the layers with ordered items.
    game.layers = [background]
    # Render the layers onto the screen.
    game.render_block()

    # Construct an infinite loop.
    while True:
        # Wait for two seconds.
        time.sleep(2.0)
        # Run the menu scene function.
        menu_scene()


# Define the menu scene function to run the starting menu.
def menu_scene():
    # Import a 16-bit bitmap image which contains
    # the background image bank for the menu.
    image_bank_mt_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a grid of the menu background with a
    # 10x8 tile grid on the PyBadge display, representing
    # its full size of 16x16 images it can contain.
    background = stage.Grid(
        image_bank_mt_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Store a list for the text objects.
    text = []
    # Create a new text object.
    text1 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text object 20 pixels
    # right and 10 pixels down.
    text1.move(20, 10)
    # Set the text to 'MT Game Studios.'
    text1.text("MT Game Studios")
    # Append the text object to the text list.
    text.append(text1)

    # Create another text object.
    text2 = stage.Text(
        width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None
    )
    # Move the text object 40 pixels
    # right and 110 pixels down.
    text2.move(40, 110)
    # Set the text to 'PRESS START.'
    text2.text("PRESS START")
    # Append the text object to the text list.
    text.append(text2)

    # Refresh the display at a 60 Hz frequency (60 FPS).
    game = stage.Stage(ugame.display, constants.FPS)

    # Set the layers with ordered items.
    game.layers = text + [background]
    # Render the layers onto the screen.
    game.render_block()

    # Construct an infinite loop.
    while True:
        # Get the user input from the
        # current buttons they are pressing.
        keys = ugame.buttons.get_pressed()

        # Check if the user pressed the
        # 'Start' button on the PyBadge.
        if keys & ugame.K_START:
            # Run the main game scene function.
            game_scene()

        # Wait for the 1/60th of a second
        # to occur for the accurate refresh
        # rate, dependent on frequency.
        game.tick()


# Define the main game scene function to run the whole game.
def game_scene():
    # Initialize a score variable.
    score = 0
    # Set a white text object for the
    # score with its size accordingly.
    score_text = stage.Text(width=29, height=14)
    # Clear the score text to update it.
    score_text.clear()
    # Move the text cursor to
    # the top-left hand corner.
    score_text.cursor(0, 0)
    # Move the text down slightly.
    score_text.move(1, 1)
    # Format the score text to
    # show the current score.
    score_text.text("Score: {0}".format(score))

    # Nest a function to take an alien off
    # the screen and prepare its position.
    def show_alien():
        # Loop over the number of
        # aliens in the alien list.
        for alien_number in range(len(aliens)):
            # Check if the current alien
            # is off the screen in the x.
            if aliens[alien_number].x < 0:
                # Move the alien to a random
                # x position and off the top
                # of the screen in the y.
                aliens[alien_number].move(
                    random.randint(
                        0 + constants.SPRITE_SIZE,
                        constants.SCREEN_X - constants.SPRITE_SIZE,
                    ),
                    constants.OFF_TOP_SCREEN,
                )
                # Break out of the for loop.
                break

    # Import a 16-bit bitmap image which contains
    # the background image bank for the game.
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    # Import another 16-bit bitmap image
    # containing the game sprites.
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # Keep initial state information for the 'A' button.
    a_button = constants.button_state["button_up"]
    # Keep initial state information for the 'B' button.
    b_button = constants.button_state["button_up"]
    # Keep initial state information for the 'Start' button.
    start_button = constants.button_state["button_up"]
    # Keep initial state information for the 'Select' button.
    select_button = constants.button_state["button_up"]

    # Initialize the 'pew' sound by opening its
    # wave file. Use 'rb' to correctly handle
    # the audio file by reading it in binary.
    pew_sound = open("pew.wav", "rb")
    # Initialize the 'boom' sound by opening its
    # wave file.
    boom_sound = open("boom.wav", "rb")
    # Initialize the 'crash' sound by opening its
    # wave file.
    crash_sound = open("crash.wav", "rb")
    # Access the game's audio.
    sound = ugame.audio
    # Stop all sounds from playing
    # to avoid unusual sound states.
    sound.stop()
    # Enable the sound, if not activated already.
    sound.mute(False)

    # Create a grid of the image background with a
    # 10x8 tile grid on the PyBadge display, representing
    # its full size of 16x16 images it can contain.
    background = stage.Grid(
        image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Loop over every column of the background grid.
    for x_location in range(constants.SCREEN_GRID_X):
        # Nest another for loop to loop over every
        # row of the current background grid column.
        for y_location in range(constants.SCREEN_GRID_Y):
            # Pick a random integer between one and
            # three to generate a random tile number.
            tile_picked = random.randint(1, 3)
            # Set the background tile to the iterated
            # location with the random tile number.
            background.tile(x_location, y_location, tile_picked)

    # Create a ship sprite by selecting the sixth
    # image off its sprite bank (0 index). Set its
    # position to 75 in the x and double its size
    # away from the bottom of the screen in the y.
    ship = stage.Sprite(
        image_bank_sprites, 5, 75, constants.SCREEN_Y - (2 * constants.SPRITE_SIZE)
    )

    # Store a list of aliens to hold them later.
    aliens = []
    # Loop over the total number of aliens.
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        # Create an alien sprite outside of the screen.
        a_single_alien = stage.Sprite(
            image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        # Append the alien to the alien list.
        aliens.append(a_single_alien)

    # Place an alien onto the screen.
    show_alien()

    # Store a list of lasers to hold them later.
    lasers = []
    # Loop over the total number of lasers.
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        # Create a laser sprite outside of the screen.
        a_single_laser = stage.Sprite(
            image_bank_sprites, 10, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
        )
        # Append the laser to the laser list.
        lasers.append(a_single_laser)

    # Refresh the display at a 60 Hz frequency (60 FPS).
    game = stage.Stage(ugame.display, constants.FPS)

    # Set the layers with ordered items.
    game.layers = [score_text] + lasers + [ship] + aliens + [background]
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
            # Check if it is the first time
            # the 'A' button has been pressed.
            if a_button == constants.button_state["button_up"]:
                # Change its button state to 'just pressed.'
                a_button = constants.button_state["button_just_pressed"]
            # Otherwise, check if the 'A' button has just been pressed.
            elif a_button == constants.button_state["button_just_pressed"]:
                # Change its button state to 'still pressed.'
                a_button = constants.button_state["button_still_pressed"]
        # Otherwise, the 'A' button was not pressed.
        else:
            # Check if the 'A' button was still pressed before.
            if a_button == constants.button_state["button_still_pressed"]:
                # Change its button state to 'released.'
                a_button = constants.button_state["button_released"]
            # Otherwise, the button was already released.
            else:
                # Change its button state to the initial state.
                a_button = constants.button_state["button_up"]
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

        # Check if the A button was 'just pressed.'
        if a_button == constants.button_state["button_just_pressed"]:
            # Loop over the number of lasers in the laser list.
            for laser_number in range(len(lasers)):
                # Check if the current laser
                # is off the screen in the x.
                if lasers[laser_number].x < 0:
                    # Move the laser to the ship's position.
                    lasers[laser_number].move(ship.x, ship.y)
                    # Play the 'pew' sound.
                    sound.play(pew_sound)
                    # Break out of the for loop.
                    break

        # Loop over the number of lasers in the laser list.
        for laser_number in range(len(lasers)):
            # Check if the current laser
            # is on the screen in the x.
            if lasers[laser_number].x > 0:
                # Move the current laser by its
                # speed up in the y direction.
                lasers[laser_number].move(
                    lasers[laser_number].x,
                    lasers[laser_number].y - constants.LASER_SPEED,
                )
                # Check if the current laser has left
                # the top of the screen in the y.
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    # Move the current laser back to its
                    # initial position off the screen.
                    lasers[laser_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
        # Loop over the number of aliens in the alien list.
        for alien_number in range(len(aliens)):
            # Check if the current alien
            # is on the screen in the x.
            if aliens[alien_number].x > 0:
                # Move the current alien by its
                # speed down in the y direction.
                aliens[alien_number].move(
                    aliens[alien_number].x,
                    aliens[alien_number].y + constants.ALIEN_SPEED,
                )
                # Check if the current alien has left
                # the bottom of the screen in the y.
                if aliens[alien_number].y > constants.SCREEN_Y:
                    # Move the current alien back to its
                    # initial position off the screen.
                    aliens[alien_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )
                    # Place an alien onto the screen.
                    show_alien()
                    # Decrement the score by one.
                    score -= 1
                    # Check if the score is negative.
                    if score < 0:
                        # Reset the score to 0.
                        score = 0
                    # Clear the score text to update it.
                    score_text.clear()
                    # Move the text cursor to
                    # the top-left hand corner.
                    score_text.cursor(0, 0)
                    # Move the text down slightly.
                    score_text.move(1, 1)
                    # Format the score text to
                    # show the current score.
                    score_text.text("Score: {0}".format(score))

        # Loop over the number of lasers in the laser list.
        for laser_number in range(len(lasers)):
            # Check if the laser is on the screen in the x.
            if lasers[laser_number].x > 0:
                # Nest another for loop to loop over the
                # number of aliens in the alien list.
                for alien_number in range(len(aliens)):
                    # Check if the alien is on the screen in the x.
                    if aliens[alien_number].x > 0:
                        # Check if the laser is colliding with the
                        # alien by using their corresponding points.
                        if stage.collide(
                            lasers[laser_number].x + 6,
                            lasers[laser_number].y + 2,
                            lasers[laser_number].x + 11,
                            lasers[laser_number].y + 12,
                            aliens[alien_number].x + 1,
                            aliens[alien_number].y,
                            aliens[alien_number].x + 15,
                            aliens[alien_number].y + 15,
                        ):
                            # Move the alien off the screen.
                            aliens[alien_number].move(
                                constants.OFF_SCREEN_X,
                                constants.OFF_SCREEN_Y,
                            )
                            # Move the laser off the screen.
                            lasers[laser_number].move(
                                constants.OFF_SCREEN_X,
                                constants.OFF_SCREEN_Y,
                            )
                            # Stop any current sounds.
                            sound.stop()
                            # Play the 'boom' sound.
                            sound.play(boom_sound)
                            # Show an alien.
                            show_alien()
                            # Show another alien.
                            show_alien()
                            # Increment the score by one.
                            score = score + 1
                            # Clear the score text to update it.
                            score_text.clear()
                            # Move the text cursor to
                            # the top-left hand corner.
                            score_text.cursor(0, 0)
                            # Move the text down slightly.
                            score_text.move(1, 1)
                            # Format the score text to
                            # show the current score.
                            score_text.text("Score: {0}".format(score))

        # Loop over the number of aliens in the alien list.
        for alien_number in range(len(aliens)):
            # Check if the alien is on the screen in the x.
            if aliens[alien_number].x > 0:
                # Check if the alien is colliding with the
                # ship by using their corresponding points.
                if stage.collide(
                    aliens[alien_number].x + 1,
                    aliens[alien_number].y,
                    aliens[alien_number].x + 15,
                    aliens[alien_number].y + 15,
                    ship.x,
                    ship.y,
                    ship.x + 15,
                    ship.y + 15,
                ):
                    # Stop all of the sounds.
                    sound.stop()
                    # Play the 'crash' sound.
                    sound.play(crash_sound)
                    # Wait for three seconds.
                    time.sleep(3.0)
                    # Run the game over scene function.
                    game_over_scene(score)

        # Render all of the sprites.
        game.render_sprites(lasers + [ship] + aliens)

        # Wait for the 1/60th of a second
        # to occur for the accurate refresh
        # rate, dependent on frequency.
        game.tick()


# Define the game over scene function
# to handle the player losing with
# their final score.
def game_over_scene(final_score):
    # Import a 16-bit bitmap image which contains
    # the background image bank for the menu.
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # Create a grid of the menu background with a
    # 10x8 tile grid on the PyBadge display, representing
    # its full size of 16x16 images it can contain.
    background = stage.Grid(
        image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y
    )

    # Store a list for the text objects.
    text = []
    # Create a new text object for the final score.
    text1 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    # Move the text object 22 pixels
    # right and 20 pixels down.
    text1.move(22, 20)
    # Set the text to the final score
    # formatted in two digits.
    text1.text("Final Score: {:0>2d}".format(final_score))
    # Append the text object to the text list.
    text.append(text1)

    # Create a second text object.
    text2 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    # Move the text object 43 pixels
    # right and 60 pixels down.
    text2.move(43, 60)
    # Set the text to 'GAME OVER.'
    text2.text("GAME OVER")
    # Append the text object to the text list.
    text.append(text2)

    # Create a third text object.
    text3 = stage.Text(
        width=29, height=14, font=None, palette=constants.BLUE_PALETTE, buffer=None
    )
    # Move the text object 32 pixels
    # right and 110 pixels down.
    text3.move(32, 110)
    # Set the text to 'PRESS SELECT.'
    text3.text("PRESS SELECT")
    # Append the text object to the text list.
    text.append(text3)

    # Refresh the display at a 60 Hz frequency (60 FPS).
    game = stage.Stage(ugame.display, constants.FPS)
    # Set the layers with ordered items.
    game.layers = text + [background]
    # Render the layers onto the screen.
    game.render_block()

    # Construct an infinite loop.
    while True:
        # Get the user input from the
        # current buttons they are pressing.
        keys = ugame.buttons.get_pressed()

        # Check if the user pressed the
        # 'Select' button on the PyBadge.
        if keys & ugame.K_SELECT:
            # Reload the game by completely
            # resetting the PyBadge.
            supervisor.reload()

        # Wait for the 1/60th of a second
        # to occur for the accurate refresh
        # rate, dependent on frequency.
        game.tick()


# Check if the special name of the file is __main__.
if __name__ == "__main__":
    # Run the splash scene function if so.
    splash_scene()
