import pygame
from pygame.sprite import Sprite
from random import randint

class Bat(Sprite):
    """A class for the enemy of the Sideways Shotoer game."""

    def __init__(self, ss_game):
        """Initialize a bat."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the bat image and get its rect.
        self.image = pygame.image.load('chapter13_exercises/images/bat.png')
        self.rect = self.image.get_rect()

        # Start each bat at a random position on the right side of the screen.
        self.rect.left = self.screen.get_rect().right

        bat_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, bat_top_max)

        # Store each bats horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bats left."""
        self.x -= self.settings.bat_speed
        self.rect.x = self.x