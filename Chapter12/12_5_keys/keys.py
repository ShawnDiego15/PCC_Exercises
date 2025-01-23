# Exercise 12-5; Keys; Page 246

# Make a Pygame file that creates an empty screen. 
# In the event loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected. 
# Run the program and press various keys to see how Pygame responds.

import sys

import pygame

from keys_settings import Settings

class KeysGame:
    """A class representing the Keys Game."""
    
    def __init__(self):
        """Initialize the Keys Game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Keys Game")

    def run_game(self):
        """Run the game."""
        while True:
            """Check events within the game."""
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            print(event.key)
            print(f"The event key for space is {event.key} while the value of pygame.K_SPACE is {pygame.K_SPACE}.")
        else:
            print(event.key)

    def _update_screen(self):
        """Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    kg = KeysGame()
    kg.run_game()