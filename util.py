#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: June 9, 2025
# This module contains utility classes
# and utility functions.

# Import the stage module for
# screen display functions.
import stage

# Import the constants module for useful constants.
import constants


# Construct a projectile class to hold projectile data.
class Projectile:
    # Define an initializer function
    # to load the object.
    def __init__(self, image_bank, tile_pos, x, y, proj_bounds, attack_pwr, proj_speed):
        # Add a projectile sprite to the object.
        self.proj_sprite = stage.Sprite(image_bank, tile_pos, x, y)
        # Add projectile boundaries to the object.
        self.min_x, self.min_y, self.max_x, self.max_y = proj_bounds
        # Add attack power to the object.
        self.attack_pwr = attack_pwr
        # Add projectile speed to the object.
        self.proj_speed = proj_speed

    # Define a function to load the projectile
    # pool and allow it to access the class.
    @classmethod
    def load_pool(cls, image_bank, tile_pos, proj_bounds, attack_pwr, proj_speed):
        # Store an empty projectile pool using a list.
        projectile_pool = []
        # Loop over the maximum pool size for projectiles.
        for proj_number in range(constants.MAX_POOL_SIZE):
            # Create a new projectile instance off the screen.
            projectile = cls(
                image_bank, tile_pos, constants.OFF_SCREEN_X,
                constants.OFF_SCREEN_Y, proj_bounds, attack_pwr, proj_speed
            )
            # Add the instance to the projectile pool.
            projectile_pool.append(projectile)
        
        # Return the projectile pool for later use.
        return projectile_pool

    # Define a function to advance the projectile.
    def advance(self):
        # Loop over the number of projectiles in the projectile pool.
        for proj_number in range(len(self)):
            # Check if the current projectile
            # is on the screen in the x.
            if self[proj_number].proj_sprite > 0:
                # Move the current projectile by its
                # speed up in the y direction.
                self[proj_number].move(
                    self[proj_number].x,
                    self[proj_number].y - self[proj_number].proj_speed,
                )
                # Check if the current projectile has left
                # the top of the screen in the y.
                if self[proj_number].y < constants.OFF_TOP_SCREEN:
                    # Move the current projectile back to its
                    # initial position off the screen.
                    self[proj_number].move(
                        constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y
                    )

    # Define a function to check projectile
    # collision with another character.
    def check_proj_collision(self, char_pool, identity):
        # Set the target character loop size.
        char_loop_size = constants.MAX_POOL_SIZE if identity == "enemy" else constants.MAX_PLAYERS

        # Loop over the number of projectiles
        # in the projectile pool.
        for proj_number in range(len(self)):
            # Check if the projectile is on the screen in the x.
            if self[proj_number].x > 0:
                # Nest another for loop to loop over the
                # number of characters, depending on the
                # character loop size.
                for char_number in range(char_loop_size):
                    # Check if the character is on the screen in the x.
                    if char_pool[char_number].x > 0:
                        # Check if the projectile is colliding with the
                        # character by using their corresponding points.
                        if stage.collide(
                            self[proj_number].proj_sprite.x + self[proj_number].min_x,
                            self[proj_number].proj_sprite.y + self[proj_number].min_y,
                            self[proj_number].proj_sprite.x + self[proj_number].max_x,
                            self[proj_number].proj_sprite.y + self[proj_number].max_y,
                            char_pool[char_number].proj_sprite.x + char_pool[char_number].min_x,
                            char_pool[char_number].proj_sprite.y + char_pool[char_number].min_y,
                            char_pool[char_number].proj_sprite.x + char_pool[char_number].max_x,
                            char_pool[char_number].proj_sprite.y + char_pool[char_number].max_y,
                        ):
                            # Take away the character's lives based
                            # on the projectile attack power.
                            char_pool[char_number].health -= self[proj_number].attack_pwr

# Construct a character class to hold character data.
class Character:
    # Define an initializer function
    # to load the object.
    def __init__(
        self, image_bank, tile_pos, x, y,
        char_bounds, lives, defense, char_speed
    ):
        # Add a character sprite to the object.
        self.char_sprite = stage.Sprite(image_bank, tile_pos, x, y)
        # Add character boundaries to the object.
        self.min_x, self.min_y, self.max_x, self.max_y = char_bounds
        # Add defense to the object.
        self.lives = lives
        # Add defense to the object.
        self.defense = defense
        # Add character speed to the object.
        self.char_speed = char_speed

# Construct a player subclass to hold player data.
# Inherits the character data.
class Player(Character):
    # Define an initializer function
    # to load the object.
    def __init__(
        self
    ):
        pass
    # Define a function to advance the projectile.
    def advance(self):
        pass



class Enemy(Character):
    pass
