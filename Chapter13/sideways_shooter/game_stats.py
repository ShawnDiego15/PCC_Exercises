# Class for Game Stats

class GameStats:
    """Track statistics for Sideways Shooter"""

    def __init__(self, ss_game):
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.bats_shot = self.settings.bats_shot