import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rd_game):
        """Initialize a raindrop."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and get its rect.
        self.image = pygame.image.load('Chapter13/images/raindrop.png')
        self.rect = self.image.get_rect()

        # Start each new Raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the Raindrop's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if raindrop is at the bottom of the screen."""
        screen_rect = self.screen.get_rect()

        if self.rect.top > screen_rect.bottom:
            return True
        else:
            return False

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.drop_speed
        self.rect.y = self.y
