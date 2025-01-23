# Exercise 12-6; Sideways Shooter

# Main File for the Jet Class

import pygame

class Jet:
    """A class to manage the jet."""

    def __init__(self, ss_game):
        """Initialze the jet and set it's starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the Jet Image and get its rect
        self.image = pygame.image.load('Chapter12/images/jet.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = ss_game.screen.get_rect()

        # Start each new Jet at the left center of the screen
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the jet's vertical position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the Jets position based on the movement flag."""
        # Update the jets y value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.jet_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.jet_speed

        # Update the rect object from self.y.
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)