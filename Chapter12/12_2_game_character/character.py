# Exercise 12-2; Game Character; Page 238

import pygame

class Character:
    """A class to manage the character."""

    def __init__(self, eg_game):
        """Initialize the character and set their starting position."""
        self.screen = eg_game.screen
        self.screen_rect = eg_game.screen.get_rect()

        # Load the character image and get its rect.
        self.image = pygame.image.load('Chapter12/images/game_character.bmp')
        self.rect = self.image.get_rect()

        # Start character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)