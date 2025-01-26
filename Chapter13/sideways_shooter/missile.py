# Exercise 12-6; Sideways Shooter;

# Main file for Missle class.

import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    """A class to manage missiles fired from the jet."""
    
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.missile_color

        # Create a missile rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.missile_width, self.settings.missile_height)
        self.rect.midright = ss_game.jet.rect.midright

        # Store the missiles position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the missiles to the right on the screen."""
        # Update the decimal position of the missile.
        self.x += self.settings.missile_speed
        # Update the rect position
        self.rect.x = self.x

    def draw_missile(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)