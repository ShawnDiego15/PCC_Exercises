# Exercise 12-6 Sideways Shooter

# Settings file for Sideways Shooter

class Settings:
    """A class to store all settings for Sideways Shooter"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Jet Settings
        self.jet_speed = 1.5

        # Missile Settings
        self.missile_speed = 1.5
        self.missile_width = 15
        self.missile_height = 3
        self.missile_color = (60, 60, 60)
        self.missiles_allowed = 5

        # Bat Settings
        self.bat_speed = 0.5
        self.bat_frequency = 0.008
        self.bats_shot = 0
