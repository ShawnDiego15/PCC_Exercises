# Exercise 12-2; Game Character; Page 238

## Game Character
#Find a bitmap image of a game character you like or convert an image to a bitmap. 
# Make a class that draws the character at the center of the screen and match the background color of the image to the background color of the screen, or vice versa.

import sys

import pygame

from character import Character

class ExerciseGame:
    """A model of a game for this exercise."""

    def __init__(self):
        """Initialize the Exercise Game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Exercise Game")

        # Set BG color
        self.bg_color = (135, 206, 235)

        # Create Character
        self.character = Character(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.character.blitme()

            pygame.display.flip()

if __name__ == '__main__':
    # Make a new game instance, and run the game.
    eg = ExerciseGame()
    eg.run_game()