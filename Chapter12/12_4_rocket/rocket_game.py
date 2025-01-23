## 12-4 Rocket; Page 246

# Make a game that begins with a rocket in the center of the screen. 
# Allow the player to move the rocket up, down, left or right using the four arrow keys. Make sure the rocket never moves beyond any edge of the screen.

import sys

import pygame

from rocket_settings import Settings
from rocket import Rocket

class RocketGame:
    """Overall class for the RocketGame"""

    def __init__(self):
        """Initialize the game."""
        pygame.init()

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self)

    def run_game(self):
        """Run the game."""
        while True:
            """Check events within the game."""
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    rg = RocketGame()
    rg.run_game()