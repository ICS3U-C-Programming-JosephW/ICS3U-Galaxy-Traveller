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
        self.proj_bounds = proj_bounds
        # Add attack power to the object.
        self.attack_pwr = attack_pwr
        # Add projectile speed to the object.
        self.proj_speed = proj_speed

    # Define a function to load the projectile
    # pool and allow it to access the class.
    @classmethod
    def load_pool():
        pass

    # Define a function to check projectile
    # collision with another character.
    def check_proj_collision(self, target_char):
        pass


# Construct a character class to hold character data.
class Character:
    # Define an initializer function
    # to load the object.
    def __init__(
        self, char_sprite, sprite_bounds, projectile, lives, defense, char_speed
    ):
        # Add the character sprite to the object.
        self.char_sprite = char_sprite
        # Add sprite boundaries to the object.
        self.sprite_bounds = sprite_bounds
        # Add the projectile to the object.
        self.projectile = projectile
        # Add lives to the object.
        self.lives = lives
        # Add defense to the object.
        self.defense = defense
        # Add the character speed to the object.
        self.char_speed = char_speed


class Player(Character):
    pass


class Enemy(Character):
    pass
