## 12-4 Rocket; Page 246

# Settings for the Rocket Game

class Settings:
    """A class to store all settings for Rocket Game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Ship Settings
        self.rocket_speed = 1.5