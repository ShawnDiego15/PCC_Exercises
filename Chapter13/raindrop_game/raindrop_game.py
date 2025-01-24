# Raindrop Game

import sys
import pygame

from raindrop_settings import Settings
from raindrop import Raindrop
from random import randint

class RaindropGame:
    """Overall class for the Raindrop Game"""

    def __init__(self):
        """Initialize the game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop Game")

        self.raindrops = pygame.sprite.Group()

        self._fill_sky()

    def run_game(self):
        """Start the main loop for the game."""
        while True:    
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        """Check keydown events, only looking to catch if 'esc' is entered."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

    def _fill_sky(self):
        """Create a sky of raindrops."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.settings.screen_width - (raindrop_width)


        self.number_raindrops_x = available_space_x // (2 * raindrop_width)

        # Determine the number of rows of raindrops that fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * raindrop_height) 

        # Create the full sky of raindrops.
        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        """Create an raindrop and place it in the row."""
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.rect.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.y = 2 * raindrop.rect.height * row_number
        raindrop.rect.y = raindrop.y

        # Randomize Position
        raindrop.rect.x += randint(-10, 10)
        raindrop.rect.y += randint(-10, 10)

        self.raindrops.add(raindrop)

    def _create_row(self, row_number):
        """Create a single row of raindrops."""
        for raindrop_number in range(self.number_raindrops_x):
            self._create_raindrop(raindrop_number, row_number)

    def _update_raindrops(self):
        """Update the Raindrops."""
        self.raindrops.update()

        make_new_drops = False
        for raindrop in self.raindrops.copy():
            if raindrop.check_edges():
                self.raindrops.remove(raindrop)
                make_new_drops = True

        # Make a new row as needed.
        if make_new_drops:
            self._create_row(0)

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    rd = RaindropGame()
    rd.run_game()