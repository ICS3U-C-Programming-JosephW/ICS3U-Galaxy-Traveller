#!/usr/bin/env python3
# Created By: Joseph Wondimagnehu
# Date: June 9, 2025
# This module contains utility classes
# and utility functions.

# Construct a character class to hold character data.
from ast import Pass


class Character:
    # Define an initializer function to
    # hold all the character attributes.
    def __init__(self, x, y, image_bank, tile_pos, image_bounds, lives, attack, defense, speed):
        # Add an x position to the object.
        self.x = x
        # Add a y position to the object.
        self.y = y
        # Add an image bank to the object.
        self.image_bank = image_bank
        # Add a tile position to the object.
        self.tile_pos = tile_pos
        # Add image boundaries to the object.
        self.image_bounds = image_bounds
        # Add lives to the object.
        self.lives = lives
        # Add attack power to the object.
        self.attack = attack
        # Add defense to the object.
        self.defense = defense
        # Add speed to the object.
        self.speed = speed
    # Define a function to deal damage to another character.
    def damage_character(image_bounds, damage):
        pass
        


class Player(Character):
    pass

class Enemy(Character):
    pass