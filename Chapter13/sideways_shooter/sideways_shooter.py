# Main file for Sideways Shooter game

import sys

import pygame
from ss_settings import Settings
from jet import Jet
from missile import Missile
from bat import Bat
from random import random

class SidewaysShooter:
    """Main class for the Sideways Shooter game"""

    def __init__(self):
        """Initialze the game."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.jet = Jet(self)
        self.missiles = pygame.sprite.Group()
        self.bats = pygame.sprite.Group()

    def run_game(self):
        """Main Loop to Run the Game."""
        while True:
            self._check_events()
            self._create_bat()
            self.jet.update()
            self._update_missiles()
            self.bats.update()
            self._remove_bats()
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
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.jet.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_missile()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.jet.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.jet.moving_down = False

    def _fire_missile(self):
        """Create a new missile and add it to the missiles group."""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _update_missiles(self):
        """Update position of missiles and get rid of old missiles."""
        # Update missile positions.
        self.missiles.update()

        # Get rid of missiles that have disappeared.
        for missile in self.missiles.copy():
            if missile.rect.left >= self.screen.get_rect().right:
                self.missiles.remove(missile)

        self._check_missile_bat_collisions()

    def _remove_bats(self):
        """Remove a bat that has reached the end of the screen."""
        for bat in self.bats.copy():
            if bat.rect.right <= self.screen.get_rect().left:
                self.bats.remove(bat)

    def _check_missile_bat_collisions(self):
        """Check if any missiles have collided with bats."""
        collisions = pygame.sprite.groupcollide(self.missiles, self.bats, False, True)


    def _create_bat(self):
        """Create a bat."""
        if random() < self.settings.bat_frequency:
            bat = Bat(self)
            self.bats.add(bat)
            print(len(self.bats))

    def _update_screen(self):
        """"Update the images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.jet.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()

        self.bats.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()
            


if __name__ == '__main__':
    # Make a new game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()