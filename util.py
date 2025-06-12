#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: June 9, 2025
# This module contains utility classes
# and utility functions.

# Import the ugame module for
# managing sounds and controls.
import ugame

# Import the stage module for
# screen display functions.
import stage

# Import the constants module for useful constants.
import constants


# Define a helper function to manage button states.
def manage_state(current_state, is_pressed):
    # Check if the button was pressed.
    if is_pressed:
        # Check if it is the first time
        # the button has been pressed.
        if current_state == constants.button_state["button_up"]:
            # Return the 'just pressed' button state.
            return constants.button_state["button_just_pressed"]
        # Return the 'still pressed' button
        # state if there was no early return.
        return constants.button_state["button_still_pressed"]
    # Otherwise, the button was not pressed.
    else:
        # Check if the button was still pressed before.
        if current_state == constants.button_state["button_still_pressed"]:
            # Return the 'released' button state.
            return constants.button_state["button_released"]
        # Return the initial button state
        # if there was no early return.
        return constants.button_state["button_up"]


# Define a helper function for checking
# if any sprite is on the screen.
def is_on_screen(sprite):
    # Return the boolean evaluation for
    # both coordinates of the sprite.
    return (constants.ORIGIN_X < sprite.x < constants.SCREEN_X) and (
        constants.ORIGIN_Y < sprite.y < constants.SCREEN_Y
    )


# Define a function to 'activate' any sprite.
def activate(sprite, target_char):
    # Move the sprite to the position
    # of the character sprite.
    sprite.move(target_char.x, target_char.y)


# Define a function to 'deactivate' any sprite.
def deactivate(sprite):
    # Move the sprite off the screen.
    sprite.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)


# Define a function to check for
# collisions between two objects.
def check_collision(main_object, target_object):
    # Check if the object sprites are on the screen.
    if is_on_screen(main_object.sprite) and is_on_screen(target_object.sprite):
        # Return True if there is a collision with the
        # object sprites by using their corresponding points.
        return stage.collide(
            main_object.sprite.x + main_object.min_x,
            main_object.sprite.y + main_object.min_y,
            main_object.sprite.x + main_object.max_x,
            main_object.sprite.y + main_object.max_y,
            target_object.sprite.x + target_object.min_x,
            target_object.sprite.y + target_object.min_y,
            target_object.sprite.x + target_object.max_x,
            target_object.sprite.y + target_object.max_y,
        )

    # Return False if there was no early return,
    # indicating that a collision did not happen.
    return False


# Construct a projectile class to hold projectile data.
class Projectile:
    # Define an initializer function
    # to load the object.
    def __init__(
        self,
        image_bank,
        tile_pos,
        x,
        y,
        bounds,
        attack_pwr,
        speed,
        owner,
        direction_x=0,
        direction_y=-1,
    ):
        # Add a projectile sprite to the object.
        self.sprite = stage.Sprite(image_bank, tile_pos, x, y)
        # Add projectile boundaries to the object.
        self.min_x, self.min_y, self.max_x, self.max_y = bounds
        # Add attack power to the object.
        self.attack_pwr = attack_pwr
        # Add projectile speed to the object.
        self.speed = speed
        # Add an x-component direction to the object.
        self.direction_x = direction_x
        # Add a y-component direction to the object.
        self.direction_y = direction_y
        # Add a character owner to the object.
        self.owner = owner

    # Define a function to load the projectile
    # pool and allow it to access the class.
    @classmethod
    def load_pool(
        cls,
        image_bank,
        tile_pos,
        bounds,
        attack_pwr,
        speed,
        owner,
        direction_x=0,
        direction_y=-1,
    ):
        # Store an empty projectile pool using a list.
        projectile_pool = []
        # Loop over the maximum pool size for projectiles.
        for proj_number in range(constants.MAX_POOL_SIZE):
            # Create a new projectile instance off the screen.
            projectile = cls(
                image_bank,
                tile_pos,
                constants.OFF_SCREEN_X,
                constants.OFF_SCREEN_Y,
                bounds,
                attack_pwr,
                speed,
                owner,
                direction_x,
                direction_y,
            )
            # Add the instance to the projectile pool.
            projectile_pool.append(projectile)

        # Return the projectile pool for later use.
        return projectile_pool

    # Define a function to advance the projectile.
    def advance(self):
        # Check if the projectile
        # is on the screen.
        if is_on_screen(self.sprite):
            # Move the projectile by its
            # direction and speed.
            self.sprite.move(
                self.sprite.x + self.direction_x * self.speed,
                self.sprite.y + self.direction_y * self.speed,
            )
        # Otherwise, the projectile
        # has left the screen.
        else:
            # Move the projectile back to its
            # initial position off the screen.
            self.sprite.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

    # Define a function to manage projectile
    # collision with another character.
    def manage_collision(self, character):
        # Check if the character is the projectile's owner.
        if character is self.owner:
            # Ignore collisions by returning False early.
            return False

        # Evaluate the collision boolean and
        # set it to the collided variable.
        collided = check_collision(self, character)

        # Check if the projectile
        # collided with the character.
        if collided:
            # Take away the character's lives
            # based on the projectile attack
            # power and character defense.
            character.lives -= self.attack_pwr / character.defense
            # Deactivate the projectile.
            deactivate(self.sprite)

        # Return the boolean result.
        return collided


# Construct a character class to hold character data.
class Character:
    # Define an initializer function
    # to load the object.
    def __init__(
        self,
        image_bank,
        tile_pos,
        x,
        y,
        bounds,
        hit_impact,
        lives,
        max_lives,
        defense,
        speed,
    ):
        # Add a character sprite to the object.
        self.sprite = stage.Sprite(image_bank, tile_pos, x, y)
        # Add character boundaries to the object.
        self.min_x, self.min_y, self.max_x, self.max_y = bounds
        # Add a hit impact to the object.
        self.hit_impact = hit_impact
        # Add lives to the object.
        self.lives = lives
        # Add maximum lives to the object.
        self.max_lives = max_lives
        # Add defense to the object.
        self.defense = max(1, defense)
        # Add character speed to the object.
        self.speed = speed

    # Define a short function that
    # checks if the character is alive.
    def is_alive(self):
        # Return True if the character's
        # lives are greater than zero.
        return self.lives > 0

    # Define a short function that
    # checks if the character is dead.
    def is_dead(self):
        # Return True if the character's lives
        # are less than or equal to zero.
        return self.lives <= 0

    # Define a short function that
    # adjusts the character's lives.
    def adjust_lives(self, amount):
        # Adjust the character's
        # lives by adding the amount
        # with boundaries.
        self.lives = max(0, min(self.lives + amount, self.max_lives))


# Construct a player subclass to hold player data.
# Additionally, it inherits the character data.
class Player(Character):
    # Define an initializer function
    # to load the object.
    def __init__(
        self,
        image_bank,
        tile_pos,
        x,
        y,
        bounds,
        hit_impact,
        lives,
        max_lives,
        defense,
        speed,
    ):
        # Call the superclass initializer
        # to get the actual character data.
        super().__init__(
            image_bank,
            tile_pos,
            x,
            y,
            bounds,
            hit_impact,
            lives,
            max_lives,
            defense,
            speed,
        )
        # Initialize the left movement flag.
        self.moving_left = False
        # Initialize the right movement flag.
        self.moving_right = False
        # Initialize the up movement flag.
        self.moving_up = False
        # Initialize the down movement flag.
        self.moving_down = False

    # Define a function to manage collisions
    # between two characters.
    def manage_collision(self, other_char):
        # Evaluate the collision boolean and
        # set it to the collided variable.
        collided = check_collision(self, other_char)

        # Check if the characters
        # collided with each other.
        if collided:
            # Take away the lives of
            # the main character based
            # on hit impact and defense.
            self.lives = max(0, self.lives - (other_char.hit_impact / self.defense))
            # Take away the lives of
            # the other character based
            # on hit impact and defense.
            other_char.lives = max(
                0, other_char.lives - (self.hit_impact / other_char.defense)
            )

        # Return the boolean result.
        return collided

    # Define a function to update the player's inputs.
    def update_input(self, keys):
        # Update the pressed status of the
        # keypad left button on the PyBadge.
        self.moving_left = keys & ugame.K_LEFT
        # Update the pressed status of the
        # keypad right button on the PyBadge.
        self.moving_right = keys & ugame.K_RIGHT
        # Update the pressed status of the
        # keypad down button on the PyBadge.
        self.moving_down = keys & ugame.K_DOWN
        # Update the pressed status of the
        # keypad up button on the PyBadge.
        self.moving_up = keys & ugame.K_UP


class Enemy(Character):
    pass
