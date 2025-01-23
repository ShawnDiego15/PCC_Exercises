# Exercise 12-1; Blue Sky; Page 238

## Blue Sky
#Make a Pygame window with a blue background.

import sys

import pygame

class ExerciseGame:
    """A model of a game for this exercise."""

    def __init__(self):
        """Initialize the Exercise Game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise Game")

        # Set BG color
        self.bg_color = (135, 206, 235)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    eg = ExerciseGame()
    eg.run_game()